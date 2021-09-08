from packagesLoader import *
from liveCommonFilesLoader import *

date_format = "%Y-%m-%d"


def sarimaForecast(originalSeries, startDate, n, p):
	print(n, p)
	currentSeries = originalSeries[:n]	
	date = pd.date_range(start=startDate, periods=n+p)
	exog = pd.DataFrame({'DATE': date})
	exog = exog.set_index(pd.PeriodIndex(exog['DATE'], freq='D'))
	for i in range(1,3):
		sin365i = 'sin365_' + str(i)
		cos365i = 'cos365_' + str(i)
		exog[sin365i] = np.sin(2 * i * np.pi * exog.index.dayofyear / 365.25)
		exog[cos365i] = np.cos(2 * i * np.pi * exog.index.dayofyear / 365.25)
	exog = exog.drop(columns=['DATE'])
	exogToTrain = exog[:n]
	exogToPredict = exog[n:n+p]
	model=pm.arima.auto_arima(currentSeries, exogenous=exogToTrain, 
		start_p=0, d=None, start_q=0, max_p=2, max_d=1, max_q=2,
		suppress_warnings =True, start_P=0, D=None, start_Q=0, max_P=2, 
		max_D=1, max_Q=2, max_order=5, seasonal=False, stepwise=True, 
		error_action="ignore")
	predictions = model.predict(p,exogenous=exogToPredict)
	return predictions.tolist()
	print('---------------------------------')

def forecastingData():
	for commodity in commodityList:
		originalFiles = [f for f in os.listdir(os.path.join('../Data/PlottingData/', commodity, 'Original'))
		if(f.endswith('csv') and not f.startswith('my') and not f.startswith('Avg_Std'))]
		l = list()
		for file in originalFiles:
			try:
				print(commodity, file)
				originalFile = os.path.join('../Data/PlottingData/', commodity, 'Original', file)
				forecastedFile = os.path.join('../Data/PlottingData/', commodity, 'Sarima', file)
				FiletoSave = forecastedFile.replace('Sarima', 'Forecast')
				originalDf = pd.read_csv(originalFile)
				originalDf = originalDf[originalDf['DATE'] >='2016-01-01' ]
				originalDf.reset_index(drop = True, inplace = True)

				forecastedDf = pd.read_csv(forecastedFile)
				forecastedDf = forecastedDf[forecastedDf['DATE'] >='2016-01-01' ]
				forecastedDf.reset_index(drop = True, inplace = True)

				cols = originalDf.columns
				startDate = originalDf['DATE'].min()
				end = originalDf.index.max()
				n = forecastedDf.index.max()
				print(n, end)
				forecastedSeries = forecastedDf[cols[1]].tolist()
				originalSeries = originalDf[cols[1]].tolist()
				while(n < end):
					if(end-n>30):
						predictions = sarimaForecast(originalSeries, startDate, n, 30)
						forecastedSeries.extend(predictions)
						print('forecasted Series:', len(forecastedSeries))
						forecastedDf = pd.DataFrame(columns = cols)
						forecastedDf[cols[0]] = pd.date_range(start=str(startDate), periods=len(forecastedSeries))
						forecastedDf[cols[1]] = forecastedSeries
						forecastedDf.to_csv(FiletoSave, index = False)
					else:
						p = end-n
						predictions = sarimaForecast(originalSeries, startDate, n, p)		
						forecastedSeries.extend(predictions)
						print('forecasted Series:', len(forecastedSeries))
						forecastedDf = pd.DataFrame(columns = cols)
						forecastedDf[cols[0]] = pd.date_range(start=str(startDate), periods=len(forecastedSeries))
						forecastedDf[cols[1]] = forecastedSeries
						forecastedDf.to_csv(FiletoSave, index = False)
					n = min(n+30, end)
				
				predictions = sarimaForecast(originalSeries, startDate, n, 30)
				forecastedSeries.extend(predictions)
				print('forecasted Series:', len(forecastedSeries))
				forecastedDf = pd.DataFrame(columns = cols)
				forecastedDf[cols[0]] = pd.date_range(start=str(startDate), periods=len(forecastedSeries))
				forecastedDf[cols[1]] = forecastedSeries	
				forecastedDf.to_csv(FiletoSave, index = False)
			except:
				l.append(file)
				continue
		print(l)