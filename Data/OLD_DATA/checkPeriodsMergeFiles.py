import pandas as pd
import os


def mergeFiles(commodity):
	folderToOpen = commodity + '/ORIGINAL/'
	files = sorted([f for f in os.listdir(folderToOpen) if (f.endswith('mandi.csv') or f.endswith('retail.csv'))])

	y = '/NormalOrAnomalous/'
	for fileName in files:
		print(fileName)
		sameMonthFile = commodity + y + 'SameMonth/' + fileName
		lastMonthFile =  commodity + y + 'LastMonth/' + fileName
		lastYearFile = commodity + y + 'LastYear/' + fileName
		maxMinFile = commodity + y + 'MaxMinRatio/' + fileName
		fileToSave = commodity + y + 'Combined/' + fileName
		sameMonthDf = pd.read_csv(sameMonthFile)
		lastMonthDf = pd.read_csv(lastMonthFile)
		lastYearDf = pd.read_csv(lastYearFile)
		maxMinDf = pd.read_csv(maxMinFile)[:len(lastMonthDf)]

		sameMonthDf['lastMonth'] = lastMonthDf['TYPE']
		sameMonthDf['lastYear'] = lastYearDf['TYPE']
		sameMonthDf['SameMonth'] = sameMonthDf['TYPE']
		sameMonthDf['MAXMINRATIO'] = maxMinDf['MAXMINRATIO']
		sameMonthDf = sameMonthDf[['STARTDATE', 'ENDDATE', 'lastMonth', 'lastYear', 'SameMonth', 'MAXMINRATIO']]
		sameMonthDf.to_csv(fileToSave, index = False)



mergeFiles('ONION')

# commodity = 'ONION'

# fileName = state + '_' + mandi + '_Price.csv'

# x = '../Data/PlottingData/'
# y = '/NormalOrAnomalous/'

# sameMonthFile = x + commodity + y + 'SameMonth/' + fileName
# lastMonthFile =  x + commodity + y + 'LastMonth/' + fileName
# lastYearFile = x + commodity + y + 'LastYear/' + fileName
# maxMinFile = x + commodity + y + 'MaxMinRatio/' + fileName


# sameMonthDf = pd.read_csv(sameMonthFile)
# lastMonthDf = pd.read_csv(lastMonthFile)
# lastYearDf = pd.read_csv(lastYearFile)
# maxMinDf = pd.read_csv(maxMinFile)[:len(lastMonthDf)]

# print(sameMonthDf.shape)
# print(lastMonthDf.shape)
# print(lastYearDf.shape)
# print(maxMinDf.shape)

# sameMonthDf['lastMonth'] = lastMonthDf['TYPE']
# sameMonthDf['lastYear'] = lastYearDf['TYPE']
# sameMonthDf['SameMonth'] = sameMonthDf['TYPE']
# sameMonthDf['MAXMINRATIO'] = maxMinDf['MAXMINRATIO']

# sameMonthDf = sameMonthDf[['STARTDATE', 'ENDDATE', 'lastMonth', 'lastYear', 'SameMonth', 'MAXMINRATIO']]

# normal = sameMonthDf[(sameMonthDf['lastMonth'] == 'Normal') & (sameMonthDf['lastYear'] == 'Normal') & (sameMonthDf['SameMonth'] == 'Normal')]




# #anomaly = sameMonthDf[(sameMonthDf['lastMonth'] == 'Anomaly') & (sameMonthDf['lastYear'] == 'Anomaly') & (sameMonthDf['SameMonth'] == 'Anomaly')]

# #anomaly = sameMonthDf[((sameMonthDf['lastMonth'] == 'Anomaly') & (sameMonthDf['SameMonth'] == 'Anomaly'))  |  ((sameMonthDf['lastMonth'] == 'Anomaly') & (sameMonthDf['lastYear'] == 'Anomaly')) |  ((sameMonthDf['SameMonth'] == 'Anomaly') & (sameMonthDf['lastYear'] == 'Anomaly'))]

# anomaly = sameMonthDf[(sameMonthDf['lastMonth'] == 'Anomaly') | (sameMonthDf['SameMonth'] == 'Anomaly') | (sameMonthDf['lastYear'] == 'Anomaly')]

# print(len(normal))
# print(len(anomaly))

# dx = normal.append(anomaly, ignore_index=True)
# dx.sort_values(['MAXMINRATIO'], inplace = True)

# fileToSave = '../Data/LeadLag/' + commodity + '/Dates/' + state + '_' + mandi + '_Normal.csv'
# print(fileToSave)
# dx.to_csv(fileToSave, index = False)
