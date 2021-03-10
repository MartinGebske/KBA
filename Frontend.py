#### Hier kommt alles rein, was mit dem Plotten zu tun hat.
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt



class Plotall:
    def __init__(self, root, size, be):
        self.be = be
        self.Cboxes = []
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

       #self.toolbar = NavigationToolbar2Tk(self.canvas, self.checkboxframe, pack_toolbar=False)
       ##        print(dir(self.toolbar))
       #self.toolbar.update()
       #self.toolbar.grid(column=0, row=1, sticky=tk.E)
        self.createWidgets(root)

    def createWidgets(self, root):
        l1 = tk.Label(self.buttonframe, text="Das ist neu: ")  #
        l1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        b1 = tk.Button(self.buttonframe, text="Select",command=self.be.getFile)
        b1.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        #b2 = tk.Button(self.buttonframe, text="BEVs Zeigen", command=self.be.requestRow)  #
        #b2.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

        #b3 = tk.Button(self.buttonframe, text="Clear", command=self.clear, activeforeground="red")
        #b3.grid(row=0, column=3, sticky=tk.N + tk.S + tk.E + tk.W)

        b4 = tk.Button(self.buttonframe, text="Close", command=root.destroy)
        b4.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

        var1 = 1
        var2 = 2
        var3 = 3
        var4 = 4
        var5 = 5
        var6 = 6



        ch1 = tk.Checkbutton(self.checkboxframe, text="BEV", variable=var1).grid(row=0, column=0, sticky=tk.W) #variable=var1 ist auch möglich im ersten ()
        ch2 = tk.Checkbutton(self.checkboxframe, text="H2", variable=var2).grid(row=1,column=0, sticky=tk.W)
        ch3 = tk.Checkbutton(self.checkboxframe, text="PHEV", variable=var3).grid(row=0,column=1, sticky=tk.W)
        ch4 = tk.Checkbutton(self.checkboxframe, text="Benzin Hybrid", variable=var4).grid(row=1,column=1, sticky=tk.W)
        ch5 = tk.Checkbutton(self.checkboxframe, text="Diesel Hybrid", variable=var5).grid(row=0,column=2, sticky=tk.W)
        ch6 = tk.Checkbutton(self.checkboxframe, text="LPG", variable=var6).grid(row=1,column=2, sticky=tk.W)
        showbutton = tk.Button(self.checkboxframe, text='Show', command=self.aquireCheckboxes).grid(row=4, sticky=tk.W, pady=4)

        self.Cboxes.append(ch1)
        self.Cboxes.append(ch2)
        self.Cboxes.append(ch3)
        self.Cboxes.append(ch4)
        self.Cboxes.append(ch5)
        self.Cboxes.append(ch6)

    def clear(self):
        self.clearplot()

    def aquireCheckboxes(self):
        for c in self.Cboxes:
            print(c.state())

    ### DAS DARF NICHT SO PASSIEREN
    def plotFigure(self,selectedList, styling):
        tspan = self.be.getTspan()

        plt.figure(figsize=(15, 5))
        plt.title("Auswahl")

        if styling:
            self.useStyle()

        plt.xticks(rotation=90, size=8)
        plt.plot(tspan, selectedList)
        plt.show()


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


