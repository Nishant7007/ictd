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




def getFinalDf(filesList, listOfDf, dates):
	for i in range(len(filesList)):
		toSave = filesList[i].replace('ORIGINAL', 'NormalOrAnomalous/MaxMinRatio')
		df = listOfDf[i]
		finalDf = pd.DataFrame(columns = ['STARTDATA', 'ENDDATA', 'MAX_PRICE', 'MIN_PRICE', 'MAXMINRATIO'])
		for date in dates:
			startDate = date[0]
			endDate = date[1]
			# print(startDate, endDate)
			dx = df[(df['DATE']>=startDate) & (df['DATE']<=endDate)]
			# print(dx)
			maxVal = dx['PRICE'].max()
			minVal = dx['PRICE'].min()
			ratio = maxVal/minVal

			finalDf = finalDf.append({'STARTDATA' : startDate,
						 'ENDDATA' : endDate,
						  'MAX_PRICE' : maxVal,
						   'MIN_PRICE' : minVal,
						    'MAXMINRATIO' : ratio},
						    ignore_index = True)
		print(toSave)
		finalDf.to_csv(toSave, index = False)



def checkPeriodsUsingMinMaxRatio(commodity):
	'''
	THIS FUNCTION IS USED TO GET THE FINAL DATAFRAMES SAVED
	IN THE RESPECTED FOLDERS
	'''
	print(commodity)
	filesList, listOfDf = getListOfDf(commodity)
	dates1 = getDatesList('2006-01-01', '2006-01-31')
	dates2 = getDatesList('2006-02-01', '2006-12-31')
	dates3 = getDatesList('2007-01-01', '2020-12-31')
	dates = dates1 + dates2 + dates3
	getFinalDf(filesList, listOfDf, dates)
	# break

checkPeriodsUsingMinMaxRatio('ONION')