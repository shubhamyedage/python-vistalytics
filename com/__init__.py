# /home/synerzip/PycharmProjects/python-vistalytics/com/resources
# import os
from os import listdir
from os.path import join, isfile, expanduser
import pandas as pd
import math

avglist3 = []
perclist3 = []
keylist = []
avglist5 = []
perclist5 = []

def averagechange(values):
    dummyvalues1 = [0 if math.isnan(x) else x for x in values]
    dummyvalues2 = [j-i for i, j in zip(dummyvalues1[:-1], dummyvalues1[1:])]
    return round(sum(dummyvalues2) / len(dummyvalues2), 2)


def percentagechange(val1, val2):
    return round((val2 - val1) * 100/val1, 2)

def processlist(values):
    avglist3.append(averagechange(values[2:]))
    perclist3.append(percentagechange(values[2], values[4]))
    avglist5.append(averagechange(values))
    perclist5.append(percentagechange(values[0], values[4]))
    return


def readfile(dirpath):
    return [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

def writefile():
    raw_data = {'Keys': keylist,
                'Average Change Over Last 3 Years': avglist3,
            'Average Change Over Last 3 Years (%)': perclist3,
            'Average Change Over Last 5 Years': avglist5,
            'Average Change Over Last 5 Years (%)': perclist5}

    outputData = pd.DataFrame(raw_data, columns=['Keys', 'Average Change Over Last 3 Years', 'Average Change Over Last 3 Years' , 'Average Change Over Last 3 Years (%)', 'Average Change Over Last 5 Years', 'Average Change Over Last 5 Years (%)'])

    outputdirpath = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "com", "output")
    outputFile = open(join(outputdirpath, "Report1.csv"), "w+")
    outputFile.close()
    outputData.to_csv(join(outputdirpath, "Report1.csv"))
    return

dirPath = join(expanduser("~"), "PycharmProjects", "python-vistalytics", "com", "resources")
print "Source Dir: " + dirPath

fileList = readfile(dirPath)
for file in fileList:
    data = pd.read_csv(join(dirPath,file), header=1, index_col=0, na_values=0)
    for index, values in data.iterrows():
        keylist.append(index)
        processlist(values)

writefile()