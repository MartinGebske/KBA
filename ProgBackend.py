import csv
import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import Utils as ut

## Hier werden datenrelevante Operationen ausgeführt.

# Listen für jeden Eintrag
bevList = []
h2List = []
phevList = []
ottoHybList = []
dieselHybList = []
lpgList = []


class myBackend():
    def __init__(self):
        self.fileVar = tk.StringVar()
        self.servingDict = {}

    # Dialogaufruf für die Auswahl der zu bearbeitenden .csv Datei
    def getFile(self):
        # Macs unterstützen nahezu keine Dropdownauswahl, weshalb hier auf das Selection Tupel verzichtet wurde
        f = filedialog.askopenfilename(title="Please select a valid .csv file")

        # Hier wird kontrolliert, ob die Dateiendung wirklich korrekt ist
        s_ext = os.path.splitext(f)
        if s_ext[1] == ".csv":
            self.fileVar.set(f)
            self.prepareFiles()
        else:
            messagebox.showerror("Wrong input file detected!", "Please select a valid .csv file")

    # Die gewählte Datei (des Kraftfahrbundesamts) muss noch weiter formatiert werden. Daher wird sie hier in eine
    # temporäre Datei geschrieben und bearbeitet.
    def prepareFiles(self):
        with open("tempfile.csv", "w") as t:
            with open(self.fileVar.get(), "r") as csv_file:
                header = next(csv_file)
                for i in csv_file:
                    i = i.strip().replace(",", ".") + "\n"
                    t.write(i)

        self.gatherRows()

    # Hier wird die neu erstellte temporäre .csv Datei ausgelesen
    def gatherRows(self):
        with open("tempfile.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            # Hier werden die Werte für die Y Achse erzeugt
            for row in reversed(list(csv_reader)):
                bevList.append(int(row[6]))
                h2List.append(int(row[7]))
                phevList.append(int(row[8]))
                ottoHybList.append(int(row[10]))
                dieselHybList.append(int(row[11]))
                lpgList.append(int(row[12]))

                # Mit diesen Daten wird nun das Dictionary befüllt, was zur Kommunikation mit dem Frontend dient
                self.servingDict["BEV"] = bevList
                self.servingDict["H2"] = h2List
                self.servingDict["PHEV"] = phevList
                self.servingDict["BenzinHybrid"] = ottoHybList
                self.servingDict["DieselHybrid"] = dieselHybList
                self.servingDict["LPG"] = lpgList

    # Das Backend kann auf diese Methode zugreifen und sich die entsprechenden Werte für die Y Achse auslesen
    def getDictEntry(self, name):
        return self.servingDict[name]

    # Hier greift das Backend auf die Utility Hilfsklasse zu und erhält die Timespan für die X Achse
    def getTspan(self):
        return ut.createTimeSpan(2016, 2021)
