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