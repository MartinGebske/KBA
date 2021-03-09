import tkinter as tk
from tkinter import filedialog, simpledialog
import json
import matplotlib as mpl
import os.path
import csv
from datetime import datetime
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
#import mplcursors  # bei Installationsfehler: pip install mplcursors --upgrade

mpl.use('TkAgg')


class Plotall:
    def __init__(self, root, size):
        mainframe = tk.Frame(root)
        mainframe.grid(row=1, rowspan=8, column=0)
        self.buttonframe = tk.Frame(root)
        self.buttonframe.grid(row=0, column=0, sticky=tk.W)
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot(111)
        # create canvas as matplotlib drawing area
        self.canvas = FigureCanvasTkAgg(self.figure, master=mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=0)  # Get reference to tk_widget
        self.toolbar = NavigationToolbar2Tk(self.canvas, mainframe, pack_toolbar=False)
        #        print(dir(self.toolbar))
        self.toolbar.update()
        self.toolbar.grid(column=0, row=1, sticky=tk.W)
        self.createWidgets(root)

    def createWidgets(self, root):
        l1 = tk.Label(self.buttonframe, text="Daten plotten: ")  #
        l1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        b1 = tk.Button(self.buttonframe, text="Select", command=self.get_data)  #
        b1.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        b2 = tk.Button(self.buttonframe, text="Plot", command=self.plotdata)  #
        b2.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
        b3 = tk.Button(self.buttonframe, text="Clear", command=self.clear, activeforeground="red")
        b3.grid(row=0, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
        b4 = tk.Button(self.buttonframe, text="Close", command=root.destroy)
        b4.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

    def plotxy(self, x, y):
        sc = self.axes.scatter(x, y)
#        cursor = mplcursors.cursor(sc,
#                                   hover=True)  # Note: mplcursors only works, when Navigation Toolbar is not active. (No Button is pressed)
        self.canvas.draw()

    def clearplot(self):
        self.toolbar.update()
        self.axes.cla()  # clear axes
        self.canvas.draw()


# HARD CODED PLOT!!!!!!!!!!!!!!!!!!!!
    def myscat(self):
        s_name, s_ext = os.path.splitext(filename.get())
        if s_ext == ".json":
            with open(filename.get()) as f:
                all_eq_data = json.load(f)
            all_eq_dicts = all_eq_data['features']
            mags, plas, lons, lats, x, y = [], [], [], [], [], []
            for eq_dict in all_eq_dicts:
                mag = eq_dict['properties']['mag']
                #                pla = eq_dict['properties']['place']
                #                lon = eq_dict['geometry']['coordinates'][0]
                lat = eq_dict['geometry']['coordinates'][1]
                mags.append(mag)
                #                plas.append(pla)
                #                lons.append(lon)
                lats.append(lat)
            x = mags[:]
            y = lats[:]
            titelstr = ".json file"

            return x, y  # , titelstr, s_ext
        elif s_ext == ".csv":
            with open(filename.get()) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                line_count = 0
                x = []
                y = []
                #
                for row in csv_reader:
                    if line_count == 0:
                        y1_lab = row[1]  # Read column title
                        y2_lab = row[2]  # Read column title
                        y3_lab = row[3]  # Read column title
                        line_count += 1
                    else:
                        date = datetime.strptime(row[2], "%Y%m%d")
                        x.append(date)
                        y.append(float(row[3]))
                        line_count += 1
            titelstr = ".csv file"
            return x, y  # , titelstr, s_ext
        else:
            res = messagebox.showerror("Programmierung mit Python", "No valid file format found!.")
            titelstr = "invalid file"
            s_ext = None
            return None, None, titelstr, s_ext

    def plotdata(self):

        x, y = self.myscat()
        self.plotxy(x, y)

    def clear(self):
        self.clearplot()

    def get_data(self):
        filename.set(filedialog.askopenfilename(initialdir="/Users/Alfa/python", title="Open Data File:", filetypes=(
            ("json files", "*.json"), ("csv files", "*.csv"), ("all files", "*.*"))))


if __name__ == "__main__":  # verhindert Start bei Import; ermöglicht Start bei Ausführung als Executable.

    root = tk.Tk()
    root.title("MyPlot")
    filename = tk.StringVar()
    plot_w = Plotall(root, (8, 6))
    root.mainloop()
