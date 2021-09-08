import os

stringToFind = 'WholesaleRaw'
def getFileNameWithString(dirName):
    # reate a list of file and sub directories 
    # names in the given directory 
    listOfFile = sorted(os.listdir(dirName))
    allFiles = list()


    








    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            getFileNameWithString(fullPath)
        else:
            if(fullPath.endswith('.py')):
                # print(fullPath)
                with open(fullPath,'rb') as f:
                    contents = f.read()
                    #print(type(contents))
                    if (bytes(stringToFind, encoding = 'utf8')) in contents:
                        print(fullPath)
                
    return allFiles

getFileNameWithString('.')


