
from packagesLoader import *
from liveCommonFilesLoader import *

# import rpy2.robjects as ro
# from rpy2.robjects.packages import importr
# from rpy2.robjects import pandas2ri

# from rpy2.robjects.conversion import localconverter

# imputeTS = importr('imputeTS')

import datetime


def getAnomaliesByVolatility(commodity, startDate):
	startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
	endDate = datetime.date(startDate.year, startDate.month, calendar.monthrange(startDate.year, startDate.month)[-1])
	volatilityList = []
	for index, row in commodityMandiDf.iterrows(): 
		state = row['STATENAME']
		mandi = row['MANDINAME']
		fileToOpen = os.path.join("../Data/PlottingData", str(commodity), 'Original', str(state)+'_'+str(mandi)+'_Price.csv')
		try:
			df = pd.read_csv(fileToOpen)
		except:
			continue
		df = df[(df['DATE']>=str(startDate)) & (df['DATE']<=str(endDate))]
		df.set_index('DATE', drop=True, inplace=True)
		val = df['PRICE'].std()/df['PRICE'].mean()
		if(mandi == mandiName):
			volatilityToCheck = val	
		else:
			volatilityList.append(val)
	if(volatilityToCheck > median(volatilityList)):
		return 'VOLATILE'
	return 'NOT VOLATILE'

vol = getAnomaliesByVolatility('BANGALORE', 'ONION', 'KARNATAKA', '2018-03-01')
print(vol)