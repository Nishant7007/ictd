
1) packageLoader.py -- will be changed to 1-packageLoader.py

# THERE ARE MANY PACKAGES USED
# THIS SCRIPT IS USED TO KEEP ALL THE IMPORT STATEMENTS IN ONE FILE
# THIS SCRIPT WILL BE THEN INMPORTED IN ALL THE SCRIPT


2) liveCommonFilesLoader.py -- will be changed to 2-commonFilesLoader.py

# There are many elements which are common to many scripts
# These elements are mandis for commodities, FCA mandis, agmarknetMandis
# This python file is used to load all these elements at once so that we don't
# have to load these elements inside each script seperately

3) liveSeperate.py -- will be changed to 3-liveSeperate.py

#THE WHOLESALE DATA IS DOWNLOADED FROM AGMARKNET MONTHLY
#THE RETAIL DATA AND WHOLESALE DATA (FOR) SOME MANDIS IS 
#DOWNLOADED FROM THE FCA WEBSITE FOR A SINGLE DAY AS A
#SINGLE FILE FOR ALL COMMODITIES
#THIS SCRIPT IS USED TO SEPERATE ALL THE DATA MANDIWISE
#(RETAIL, WHOLESALE, ARRIVAL DATA FOR EACH MANDI)


4) fillMissingValues.py -- will be changed to 4-fillMissingValues.py

# THIS FILE WILL TAKE ALL THE FILES IN THE Nans_Data FOLDER IN EACH COMMODITY FOLDER
# AND USE STINEMAN INTERPOLATION TO FILL MISSING VALUES. THE OUTPUT FILES WILL BE
# STORED IN Original FOLDER IN EACH COMMODITY FOLDER


5) removeIrrelevantMandis.py

# INTIALLY WE CONSIDERED MANY MANDIS BUT AS FORECASTING TAKES TOO MUCH TIME
# SO WE REMOVED SOME OF THE MANDIS TO MANAGE THE DATA WELL
# THIS SCRIPT IS WRITTEN FOR THAT PURPOSE

6) findingNeighbouringMandi.py

# THIS SCRIPT IS FIND THE NEIGHBOURING MANDI FOR EACH GIVEN MANDI USING MAXIMUM 
# CORRELATION BETWEEN MANDIS AND THEN SAVE THE MANDI-NEIGHBOURING MANDI AS A CSV FILE.


7) findNextDateAG.py

# THIS FUNCTION IS USED TO FIND THE LAST DATE FOR THE AVAILABLE DATA FOR EACH STATE. 
# THE NEXT TIME THE DATA WILL BE DOWNLOADED FOR THIS MONTH


# ------------------------------------------------------------------------------


8) volatility.py:
# THIS SCRIPT IS USED TO CALCULATE VOLATILITY
#	1. calcVolatiltiy(name)
#   		FIND THE VOLATILITY FOR EACH MONTH FOR ALL THE COMMODITIES GIVEN THE
#     		TYPE OF DATA (MANDI PRICE OR RETAIL)

#	2. mostVolatileMandisForMonth(commodity ,year, month)
#    		FIND THE MOST VOLATILITY MANDIS FOR EACH MONTH FOR GIVEN COMMODITY
#    		MONTH AND YEAR. THIS FUNCTION WILL BE CALLED BY findMostVolatileMandis()

#	3. findMostVolatileMandis():
#    		GENERATING ALL THE MONTH AND YEAR COMBINATIONS AND RUN THE 	
# 			mostVolatileMandisForMonth(commodity ,year, month)
#    		FOR EACH COMBINATION OF COMMODITY, MONTH AND YEAR
#       --
#       --
#		IT WILL SAVE THE FILES IN THE VOLATILITY FOLDER INSIDE EACH COMMODITY FOLDER



9) dispersion.py:
#   THIS SCRIPT IS USED TO CALCULATE DISPERSION	
#	1. calcDispersion():
#			CALCULATE DISPERSION FOR ALL DATA (MANDI, RETAIL OR ARRIVAL)
#			IT WILL CALL calcDispersionForName()	
#	2. calcDispersionForName():
#			CALCULATE DISPERSION FOR GIVEN TYPE OF DATA (MANDI, RETAIL OR ARRIVAL)
#


10) findAnomalousMandisCentres.py:
#	this script find the the anomalous mandi/centre using the
#	previous 6 months anomalies

11) findAnomalousCommodities.py:
#	this script finds the most anomalous commodities using the 
#	previous 6 months anomalies

1) nameChanger.py -- replace .csv.csv with .csv in file name in wholesaleraw data

2) liveFormatWholesaleData.py -- format files in 'WholesaleRaw' by using ffill() and save in 'Wholesale'

3) findAllFiles.py -- get name of all the files in the given directory


4) liveInformation.py -- get the information about states, csntres, mandis



5) getAnomalyDates.py -- 
#			THIS SCRIPT IS USED TO GET THE ANOMALY DATES
#			THE ANOMALIES ARE MARKED USING THE NEWS ARTICLES
#			WE MARK THE DATES WITH NEWS ARTICLES AND THEN TAKE THE MINIMUM/MAX
#			PRICE IN THE IN LAST 14 DAYS AND THEN TAKE THAT DATE AS NEW DATE OF
#			THE ANOMALY


6) checkPeriodsUsingLastYear.py --
#	USED TO CHECK IF A PERIOD IS ANOMALOUS OR NOT BASED ON RULES
#	RULES ARE: LAST MONTH, LAST YEAR, SAME MONTH
#	THE PERIODS WHICH ARE MARKED NORMAL WILL BE USED TO FIND FINAL NORMAL PERIODS
#	THE ANOMALOUS PERIOD WILL NOT BE USED ANYWHERE RIGHT NOW .. 


7) mergeNewsFiles.py --
#	FOR A GIVEN COMMODITY, THERE ARE MANY NEWS FILE FOR EACH YEAR BECAUSE WE SPLITTED THE DATA INITIALLY BECAUSE OF LARGE SIZE. THIS SCRIPT IS USED TO MERGE ALL THOSE FILES AND STORE THE FILES IN Data/News/Merged folder...  INPUT IS TAKEN FROM THE SPLIT FOLDER

8) newsfilter.PY --

# THIS FILE IS USED TO APPLY THE FILTER BASED ON THE KEYWORDS TO FIND THE TOP RELEVANT KEYWORDS. THE KEYWORD FILE IN PRESENT IN SAME FOLDER IN newsKeywords file


9) checkPeriodsMergeFiles.py -- 
#MERGE FILES CREATED BY 4 SCRIPTS:
#	checkPeriodsUsingLastMonth.py
#	checkPeriodsUsingLastYear.py
#	checkPeriodsUsingSameMonth.py
#	checkPeriodsUsingMaxMin.py


10) generateNewsFeed.py --
#generateVolatilityNews()
#generateMandiAnomalousNews()-- generate three type of files for news articles related to mandis data -------- anomalousAndArticle, notAnomalousAndArticle, anomalousAndNoArticle

#generateRetailAnomalousNews()-- generate three type of files for news articles related to retail centre data -------- anomalousAndArticle, notAnomalousAndArticle, anomalousAndNoArticle

	
