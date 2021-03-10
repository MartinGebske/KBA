#### Hier kommt alles rein, was mit dem Plotten zu tun hat.
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

Cboxes = {}
class Plotall:

    def __init__(self, root, size, be):
        self.be = be
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

        self.checkboxframe = tk.Frame(mainframe)
        self.checkboxframe.grid(row=1, column= 0, sticky=tk.W)

        self.createWidgets(root)

    def createWidgets(self, root):
        l1 = tk.Label(self.buttonframe, text="Das ist neu: ")  #
        l1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        b1 = tk.Button(self.buttonframe, text="Select",command=self.be.getFile)
        b1.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        b4 = tk.Button(self.buttonframe, text="Close", command=root.destroy)
        b4.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

        allEntries = ["BEV", "H2", "PHEV", "BenzinHybrid", "DieselHybrid","LPG"]
        for j in allEntries:
            Cboxes[j] = tk.IntVar(0)

        tk.Checkbutton(self.checkboxframe, text="BEV", variable=Cboxes[allEntries[0]]).grid(row=0, column=0, sticky=tk.W) #variable=var1 ist auch möglich im ersten ()
        tk.Checkbutton(self.checkboxframe, text="H2", variable=Cboxes[allEntries[1]]).grid(row=1,column=0, sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="PHEV", variable=Cboxes[allEntries[2]]).grid(row=0,column=1, sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="Benzin Hybrid", variable=Cboxes[allEntries[3]]).grid(row=1,column=1, sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="Diesel Hybrid", variable=Cboxes[allEntries[4]]).grid(row=0,column=2, sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="LPG", variable=Cboxes[allEntries[5]]).grid(row=1,column=2, sticky=tk.W)
        tk.Button(self.checkboxframe, text='Show', command=self.aquireCheckboxes).grid(row=4, sticky=tk.W, pady=4)



    def clear(self):
        self.clearplot()

    def aquireCheckboxes(self):
        self.axes.cla()
        tspan = self.be.getTspan()


        #yAxis = self.be.getDictEntry("BEV")
        #self.axes.plot(tspan,yAxis)
        #self.canvas.draw()

        for i,j in Cboxes.items():
            if Cboxes[i].get() == 1:
                self.axes.plot(tspan, self.be.getDictEntry(i))
        self.canvas.draw()

        #self.figure.draw()


        #self.useStyle()

        #plt.xticks(rotation=90, size=8)
        #plt.show()



    def useStyle(self):
        """[INFO: ] Styling will remove top and right spines
        of plot and apply vertical lines to visualize single
        years more clearer"""
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        i = 0
        while i <= 60:
            plt.axvline(i, alpha=0.25, c="gray")
            i += 12


