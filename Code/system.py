
from packagesLoader import *
import pickle

# from nameChanger import *
# from liveFormatWholesaleData import *
from liveProcessData import *
# from liveWholesaleCrawler import *
# from liveSystemFunctions import *
from liveCommonFilesLoader import *

# print('Loading Data Dictionary')
# d = pickle.load(open('myDicts.p','rb'))

# print('Data dictionary before all work')
# print(d)

wholesaleRawDirectory = '../Data/Original/WholesaleRaw'
wholesaleDirectory = '../Data/Original/Wholesale'
processedWholesaleDirectory = '../Data/Processed/Wholesale'

CommodityStateFiles = []
for k in dictAG['commodity'].keys():
        for x in dictAG['commodity'][k]:
                CommodityStateFiles.append(k+'/'+x)

## print('Download Wholesale Data')
# d['MonthsDict'] = wholesaleDataCrawler(d['MonthsDict'])

# print('remove extra .csv from whoesale files')
# nameChangerFunction(wholesaleRawDirectory)

# print('formatting the wholesalefiles')
# formatData(wholesaleRawDirectory)
for k in dictAG['commodity'].keys():
        for x in dictAG['commodity'][k]:
                CommodityStateFiles.append(k+'/'+x)


# print('Download Wholesale Data')
# d['MonthsDict'] = wholesaleDataCrawler(d['MonthsDict'])

# print('remove extra .csv from whoesale files')
# nameChangerFunction(wholesaleRawDirectory)

# print('formatting the wholesalefiles')
# formatData(wholesaleRawDirectory)

# print('Processing wholesale data')
#print(CommodityStateFiles)
processWholesaleData(CommodityStateFiles)

#print('edit names of processed wholesale files')
#editNamesFunction(processedWholesaleDirectory)

#print('Seperating Price and Arrival Files')
#seperateFiles()

#print('Seperate Final Price and Arrival Data')
#makeArrivalFiles()
#makePriceFiles()
#print('Final Price and Arrival Data Seperated')
























from packagesLoader import *
