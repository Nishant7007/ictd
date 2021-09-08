import os
import pandas as pd
import datetime           
from dateutil.relativedelta import * 
from datetime import timedelta
import numpy as np
from statistics import mean, median


def readCSV(x):
	'''
	FUNCTION FOR READING DFs
	'''
	return pd.read_csv(x)


def getListOfDf(commodity):
	'''
	THIS WILL RETURN LIST OF DFs FOR ALL MANDIS FOR A COMMODITY
	THIS WILL RETURN LIST OF FILE NAMES FOR ALL MANDIS FOR A COMMODITY
	'''
	folder = '/'.join([commodity, 'ORIGINAL'])
	files = sorted([f for f in os.listdir(folder) if (f.endswith('mandi.csv') or f.endswith('retail.csv'))])
	filesList = [os.path.join(folder, file) for file in files]
	listOfDf = list(map(readCSV, filesList))
	return filesList, listOfDf


def getDatesList(startDate, endDate = '2020-12-31'):
	'''
	RETURN A LIST OF LIST OF DATES BETWEEN startDate AND endDate
	EACH ELEMENT IN LIST IS A LIST OF TWO DATES SEPERATED BY 43 DAY WINDOW
	INCRFMENT IF FOR 7 DAYS 
	'''
	dates = (pd.date_range(start = startDate, end = endDate, freq = '7D')).strftime('%Y-%m-%d').tolist()
	dates = [datetime.datetime.strptime(x, '%Y-%m-%d') for x in dates]
	dates = [[datetime.datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'), datetime.datetime.strptime(str(x+timedelta(43)), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')] for x in dates]
	return dates


def getMedianOfList(l):
	'''
	RETURN MEDIAN OF A LIST
	'''
	return median(l)


def getMedian(df, startDate, endDate):
	'''
	GIVEN A DFs RETURN MEDIAN OF ALL VALUES BETWEEN startDate AND endDate
	'''
	df = df[(df['DATE']>=startDate) & (df['DATE']<endDate)]
	if(len(df)<=0):
		return np.nan
	return getMedianOfList(df['PRICE'].tolist())


def getMediansAndMadforLastYear(dates, listOfDf):
	'''
	RETURN A DICT OF DATES AND MEDIAN AND MAD VALUE
	KEY : STARTDATE
	VALUE : [ENDDATE, MEDIAN FOR DF BETWEEN STARTDATE AND ENDDATE, MODE FOR DF BETWEEN STARTDATE AND ENDDATE]
	'''
	dict = {}
	for date in dates:
		startDate, endDate = date[0], date[1]
		lastYearstartDate = str((datetime.datetime.strptime(startDate, '%Y-%m-%d') + relativedelta(years = -1)).strftime('%Y-%m-%d'))
		lastYearEndDate = str((datetime.datetime.strptime(endDate, '%Y-%m-%d') + relativedelta(years = -1)).strftime('%Y-%m-%d'))
		listOfMedians = list(map(lambda x: getMedian(x, lastYearstartDate, lastYearEndDate), listOfDf))
		if(not np.isnan(listOfMedians[0])):
			dict[startDate] = [endDate, median(listOfMedians), pd.Series(listOfMedians).mad()]	
	return dict


def getMediansforThisYear(dates, listOfDf):
	'''
	RETURN A DICT OF DATES AND MEDIAN AND MAD VALUE
	KEY : STARTDATE
	VALUE : MEDIAN FOR DF BETWEEN STARTDATE AND ENDDATE
	'''
	dict = {}
	for date in dates:
		startDate, endDate = date[0], date[1]
		listOfMedians = list(map(lambda x: getMedian(x, startDate, endDate), listOfDf))
		if(not np.isnan(listOfMedians[0])):
			dict[startDate] = listOfMedians	
	return dict


def isAnomalous(val, median, mad):
	'''
	CHECK IF A VALUE IS OUTSIDE MADs FROM MEDIAN
	'''
	if((val<=(median-1.48*mad)) or (val>=(median+1.48*mad))):
		return 'Anomaly'
	else:
		return 'Normal'


def getFinalDict(thisYearMedianDict, lastYearMedianDict):
	'''
	GIVEN TWO DICTS:
	thisYearMedianDict AND lastYearMedianDict
	RETURN A finalDict WITH KEY = startDate
	AND VALUE AS A LIST OF [endDate, thisYearNormal, median, mad, thisYearMedianDict[k] (MEDIAN VALUE FOR THIS YEAR)]
	'''
	finalDict = {}
	for k in thisYearMedianDict.keys():
		startDate = k
		endDate = lastYearMedianDict[k][0]
		median = lastYearMedianDict[k][1]
		mad = lastYearMedianDict[k][2]
		thisYearNormal = list(map(lambda val: isAnomalous(val, median, mad), thisYearMedianDict[k]))
		finalDict[startDate] = [endDate, thisYearNormal, median, mad, thisYearMedianDict[k]]
	return finalDict




def getDfForOldDates(startDate, endDate):
	'''
	RETURN A DF WITH STARTDATE, ENDDATE, MEDIAN, MAD, VALUE, TYPE AS COLUMNS FOR
	DATES WHOSE ANOMALY CANNOT BE FOUND (2016 IN THIS CASE)
	'''
	oldStartDate = str((datetime.datetime.strptime(startDate, '%Y-%m-%d') + relativedelta(years = -1)).strftime('%Y-%m-%d'))
	oldEndDate = str((datetime.datetime.strptime(startDate, '%Y-%m-%d') + relativedelta(days = -1)).strftime('%Y-%m-%d'))	
	oldDates = getDatesList(startDate = oldStartDate, endDate = oldEndDate)
	sDates = []
	eDates = []
	for each in oldDates:
		sDates.append(each[0])
		eDates.append(each[1])
	dk = pd.DataFrame({'STARTDATE' : sDates,
		   'ENDDATE' : eDates,
		   'MEDIAN' : np.nan,
		   'MAD' : np.nan,
		   'VALUE' : np.nan,
		   'TYPE' : np.nan})
	return dk


def dfForCurrentDates(filesList, finalDict, i):
	'''
	RETURN A DF WITH STARTDATE, ENDDATE, MEDIAN, MAD, VALUE, TYPE AS COLUMNS FOR
	DATES WHOSE ANOMALY CAN BE FOUND (2017-2020 IN THIS CASE)
	'''
	startDates, endDates, periods, lastYearMedians, lastYearMads, thisyearMedians = ([] for i in range(6))
	for k in finalDict.keys():
		startDate = k
		endDate = finalDict[k][0]
		period = finalDict[k][1][i]
		lastYearMedian = finalDict[k][2]
		lastYearMad = finalDict[k][3]
		thisyearMedian = finalDict[k][4][i]

		startDates.append(startDate)
		endDates.append(endDate)
		periods.append(period)
		lastYearMedians.append(lastYearMedian)
		lastYearMads.append(lastYearMad)
		thisyearMedians.append(thisyearMedian)

	
	dfDict = {'STARTDATE' : startDates,
		   'ENDDATE' : endDates,
		   'MEDIAN' : lastYearMedians,
		   'MAD' : lastYearMads,
		   'VALUE' : thisyearMedians,
		   'TYPE' : periods}
	dx = pd.DataFrame(dfDict)
	return dx, startDates, endDates


def getFinalDf(filesList, finalDict):
	'''
	GOING TO EACH FILE IN THE LIST OF FILES IN A COMMODITY AND MERGE
	THE DFs RETURNED BY getDfForOldDates AND dfForCurrentDates
	'''
	for i in range(len(filesList)):
		print(filesList[i])

		dx, startDates, endDates = dfForCurrentDates(filesList, finalDict, i)
		dk = getDfForOldDates(startDate = startDates[0], endDate = endDates[0])
		
		dx = dk.append(dx, ignore_index=True)

		fileToSave = filesList[i].replace('ORIGINAL', 'NormalOrAnomalous/LastYear')
		print(fileToSave)
		print(len(dx), len(dx[dx['TYPE']=='Normal']), len(dx[dx['TYPE']=='Anomaly']))		
		
		dx.to_csv(fileToSave, index = False)


def checkPeriodsUsingLastyear(commodity):
	'''
	THIS FUNCTION IS USED TO GET THE FINAL DATAFRAMES SAVED
	IN THE RESPECTED FOLDERS
	'''
	print(commodity)
	filesList, listOfDf = getListOfDf(commodity)
	dates = getDatesList('2007-01-01', '2020-12-31')
	lastYearMedianDict = getMediansAndMadforLastYear(dates, listOfDf)

	thisYearMedianDict = getMediansforThisYear(dates, listOfDf)

	finalDict = getFinalDict(thisYearMedianDict, lastYearMedianDict)
	getFinalDf(filesList, finalDict)

checkPeriodsUsingLastyear('POTATO')