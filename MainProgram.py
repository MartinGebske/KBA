#### Hier kommt alles zusammen...

import csv
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.rrule import rrule, MONTHLY



myTimespan = []

##ALL COLUMNS:

totalAlternatives=[] #row1
bevList = [] #row6
h2List = [] #row7
phevList = [] #row8
ottoHybList = [] #row10
dieselHybList = [] #row11
lpgList = [] #row12

titles = []

## CREATE TIMESPAN ##

startDate = dt.date(2016, 1, 1)
endDate = dt.date(2021, 1, 1)

dates = [d for d in rrule(MONTHLY, dtstart=startDate, until=endDate)]

for d in dates:
    cur = dt.date.strftime(d, "%b-%y")
    myTimespan.append(str(cur))


## READ FILE AND FILL LISTS ###

l = 0
with open("KBA_Zulassungen.csv", "r", encoding="utf-8") as csv_file:
        l = sum(1 for row in csv_file)


with open("KBA_Zulassungen.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    count = 0
    for row in reversed(list(csv_reader)):
        count += 1

        totalAlternatives.append(int(row[1]))
        bevList.append(int(row[6]))
        h2List.append(int(row[7]))
        phevList.append(int(row[8]))
        ottoHybList.append(int(row[10]))
        dieselHybList.append(int(row[11]))
        lpgList.append(int(row[12]))

        if count == l - 1:
            break


## PLOT STUFF ###

def plotFigure(selectedList, styling):

    plt.figure(figsize=(15, 5))
    plt.title("Auswahl")

    if styling:
        useStyle()

    plt.xticks(rotation=90, size=8)
    plt.plot(myTimespan, selectedList)
    plt.show()


def useStyle():
    """[INFO: ] Styling will remove top and right spines
    of plot and apply vertical lines to visualize single
    years more clearer"""
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    i = 0
    while i <= 60:
        plt.axvline(i, alpha=0.25, c="gray")
        i += 12

def selectData(number):

    selector ={
        1 : totalAlternatives,
        2 : bevList

    }
    plotFigure(selector.get(number),styling=True)
    # help(useStyle)

selectData(1)