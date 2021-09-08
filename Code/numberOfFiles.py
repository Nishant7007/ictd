from packagesLoader import *



for commodity in sorted(commodityList):
	folderToOpen = "../Data/PlottingData/" + commodity + '/Original'
	n = len(os.listdir(folderToOpen))
	print(commodity, n)