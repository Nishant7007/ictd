import pandas as pd
import os
import numpy as np

def checkIfDecimal(x):
    return (int(str(x).split('.')[1]) != 0)

mandiFiles = [f for f in os.listdir() if f.endswith('mandi.csv')]
retailFiles = [f for f in os.listdir() if f.endswith('retail.csv')]
arrivalFiles = [f for f in os.listdir() if f.endswith('arrival.csv')]


for file in arrivalFiles:
	fileToSave = '../Temp/' + file
	df = pd.read_csv(file, header = None)
	mask = df[1].apply(lambda x: True if checkIfDecimal(x) else False)
	df[1][mask] = np.nan
	print(df.head())
	df.columns = ['DATE', 'ARRIVAL']
	df.to_csv(fileToSave, index = False)