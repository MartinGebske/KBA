import csv
import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import Utils as ut

#myLists = {
#"bevList" : [],  # row6
#"h2List" : [],  # row7
#"phevList" : [],  # row8
#"ottoHybList" : [],  # row10
#"dieselHybList" : [],  # row11
#"lpgList" : []  # row12
#}


bevList = []  # row6
h2List = []  # row7
phevList = [] # row8
ottoHybList = []  # row10
dieselHybList = []  # row11
lpgList = []  # row12



class myBackend():
    def __init__(self):
        self.tempTitles = []
        self.fileVar = tk.StringVar()
        #self.testList = []
        self.testDict = {}
        #self.tspan= ut.createTimeSpan(2016,2021)

    def getFile(self):
        f = filedialog.askopenfilename(title="Please select a valid .csv file")
        s_ext = os.path.splitext(f)
        if s_ext[1] == ".csv":
            self.fileVar.set(f)
            self.prepareFiles()
            self.gatherRows()
        else:
            messagebox.showerror("Program error!", "No valid file format found!")

    def prepareFiles(self):
        with open("tempfile.csv", "w") as t:
            with open(self.fileVar.get(), "r") as csv_file:
                header = next(csv_file)
                for i in csv_file:
                    i = i.strip().replace(",", ".") + "\n"
                    t.write(i)
            for i in header:
                self.tempTitles.append(i)
            #print(self.tempTitles)

    def getTspan(self):
        return ut.createTimeSpan(2016,2021)

    def gatherRows(self):
        print("Hier kommen die Reihen")
        with open("tempfile.csv", "r") as csv_file:  # Hier bekommen wir die Werte für die Y Achse
            csv_reader = csv.reader(csv_file, delimiter=";")
            for row in reversed(list(csv_reader)):
                bevList.append(int(row[6]))
                h2List.append(int(row[7]))
                phevList.append(int(row[8]))
                ottoHybList.append(int(row[10]))
                dieselHybList.append(int(row[11]))
                lpgList.append(int(row[12]))

                #self.testList.append(bevList)
                #self.testList.append(h2List)
                #self.testList.append(phevList)
                #self.testList.append(ottoHybList)
                #self.testList.append(dieselHybList)
                #self.testList.append(lpgList)

                self.testDict["BEV"] = bevList
                self.testDict["H2"] = h2List
                self.testDict["PHEV"] = phevList
                self.testDict["BenzinHybrid"] = ottoHybList
                self.testDict["DieselHybrid"] = dieselHybList
                self.testDict["LPG"] = lpgList
        print(self.testDict)

    def getDictEntry(self, name):
        return self.testDict[name]

