import pandas as pd
import numpy as np
import time
import os
import math
from stineman import *

def fillMissingValues(commodity):
	startTime = time.time()
	folderToOpen = commodity+'/NANS_DATA'
	files = sorted(os.listdir(folderToOpen))

	for file in files:
		fileToOpen = os.path.join(folderToOpen, file)
		fileToSave = fileToOpen.replace('NANS_DATA', 'ORIGINAL')
		print(fileToOpen)
		print(fileToSave)

		df = pd.read_csv(fileToOpen)
		cols = df.columns
		col0 = cols[0]
		col1 = cols[1]
		df[col1].replace(0.0, np.nan, inplace=True)
		print(df.head(10))
		x = 0
		for index, row in df.iterrows():
			if(math.isnan(row[col1])):
				x+=1
			else:
				val = row[col1]
				break
		while(x>=0):
			df.loc[x, col1] = val
			x-=1

		df.reset_index(inplace=True)
		df['x'] = [i for i in range (df.shape[0])]
		xi = np.array(df['x'])
		df = df[df[cols[1]].notna()]
		x = np.array(df['x'])
		y = np.array(df[cols[1]])
		yp = None 
		yi = (stineman_interp(xi,x,y,yp)).tolist()
		df1 = pd.DataFrame({col1:yi})
		df1[col0] = pd.date_range(start = '2006', periods=len(df1), freq='D')
		col0, col1 = col1, col0
		df1 = df1[cols]
		df1.interpolate(inplace=True)
		print(df1.head(10))
		df1.to_csv(fileToSave, index=False)
	print(time.time()-startTime)

fillMissingValues('ONION')