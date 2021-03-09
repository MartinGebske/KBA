import csv
import tkinter as tk
import Utils as ut
import PlotManager as pm
import os.path
from tkinter import filedialog, messagebox

totalAlternatives = []  # row1
bevList = []  # row6
h2List = []  # row7
phevList = []  # row8
ottoHybList = []  # row10
dieselHybList = []  # row11
lpgList = []  # row12

titles = []

root = tk.Tk()
root.withdraw()
fileVar = tk.StringVar()


# BEDENKE: Es gibt Probleme mit dem Askopenfilename unter mac.
def getFile():
    f = filedialog.askopenfilename(title="Please select a valid .csv file")
    root.destroy()
    s_ext = os.path.splitext(f)
    if s_ext[1] == ".csv":
        fileVar.set(f)
    else:
        messagebox.showerror("Program error!", "No valid file format found!")


def selectData(number):
    myTimespan = ut.createTimeSpan(2016, 2021)  # DAS ist die X Achse

    selector = {
        1: totalAlternatives,
        2: bevList
    }

    with open("tempfile.csv", "w") as t:
        with open(fileVar.get(), "r") as csv_file:
            for i in csv_file:
                i = i.strip().replace(",", ".") + "\n"
                t.write(i)

    with open("tempfile.csv", "r") as csv_file:  # Hier bekommen wir die Werte für die Y Achse
        csv_reader = csv.reader(csv_file, delimiter=";")
        header = next(csv_reader)
        for row in reversed(list(csv_reader)):
            totalAlternatives.append(int(row[1]))
            bevList.append(int(row[6]))
            h2List.append(int(row[7]))
            phevList.append(int(row[8]))
            ottoHybList.append(int(row[10]))
            dieselHybList.append(int(row[11]))
            lpgList.append(int(row[12]))

    for i in header:
        titles.append(i)
    pm.plotFigure(myTimespan, selector.get(number), styling=True)
    root.quit()


### THIS IS WHERE THE MAGIC HAPPENS...
getFile()

selectData(2)

root = tk.Tk()
root.withdraw()

root.mainloop()
