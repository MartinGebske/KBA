import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

Cboxes = {}


## Diese Klasse ist für die visuelle Darstellung zuständig

class Plotall:

    def __init__(self, root, size, be):
        self.be = be
        self.timespan = self.be.getTspan()

        # Das Hauptfenster für die Anwendung
        mainframe = tk.Frame(root)
        mainframe.grid(row=1, rowspan=8, column=0)

        # Buttons für den Programmeinstieg
        self.buttonframe = tk.Frame(root)
        self.buttonframe.grid(row=0, column=0, sticky=tk.W)

        # Definition des einzubettenden Plot
        self.figure = plt.Figure(size)
        self.axes = self.figure.add_subplot(111)

        # (Initiale) Einbettung des Plots
        self.canvas = FigureCanvasTkAgg(self.figure, master=mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=0)

        # Checkboxen zum Durchschalten der angezeigten Daten
        self.checkboxframe = tk.Frame(mainframe)
        self.checkboxframe.grid(row=1, column=0, sticky=tk.W)

        # Erstellungsmethode für die zuvor definierten Frames
        self.createWidgets(root)

    def createWidgets(self, root):
        # Erstellung der UI Elemente
        l1 = tk.Label(self.buttonframe, text="Treffen Sie eine Auswahl: ")
        l1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        b1 = tk.Button(self.buttonframe, text="Datei...", command=self.be.getFile)
        b1.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        b4 = tk.Button(self.buttonframe, text="Beenden", command=root.destroy)
        b4.grid(row=0, column=4, sticky=tk.N + tk.S + tk.E + tk.W)

        # Liste aller bekannten Bezeichnungen
        allEntries = ["BEV", "H2", "PHEV", "BenzinHybrid", "DieselHybrid", "LPG"]

        # Dem Cboxes Dictionary werden anhand der allEntries Werte IntVar Variablen zugeordnet
        for j in allEntries:
            Cboxes[j] = tk.IntVar(0)

        # Jede Bezeichnung erhält eine Checkbox. In der Variable wird 1 (aktiv) oder 0 (inaktiv) gespeichert
        tk.Checkbutton(self.checkboxframe, text="BEV", variable=Cboxes[allEntries[0]]).grid(row=0, column=0,
                                                                                            sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="H2", variable=Cboxes[allEntries[1]]).grid(row=0, column=1, sticky=tk.W)

        tk.Checkbutton(self.checkboxframe, text="PHEV", variable=Cboxes[allEntries[2]]).grid(row=0, column=2,
                                                                                             sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="Benzin Hybrid", variable=Cboxes[allEntries[3]]).grid(row=1, column=0,
                                                                                                      sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="Diesel Hybrid", variable=Cboxes[allEntries[4]]).grid(row=1, column=1,
                                                                                                      sticky=tk.W)
        tk.Checkbutton(self.checkboxframe, text="LPG", variable=Cboxes[allEntries[5]]).grid(row=1, column=2,
                                                                                            sticky=tk.W)
        # Über diesen Button wird das Plotten aufgerufen
        tk.Button(self.checkboxframe, text='Auswahl anzeigen', command=self.aquireCheckboxes).grid(row=4, sticky=tk.W,
                                                                                                   pady=4)

    def aquireCheckboxes(self):
        # Bei jedem Aufruf der Methode wird die Figure gecleared.
        self.axes.cla()
        tspan = self.be.getTspan()

        # Hier wird über das Cboxes Dictionary iteriert. Wenn eine Checkbox aktiv ist,
        # werden beim Backend die entsprechenden Werte abgefragt.
        for i, j in Cboxes.items():
            if Cboxes[i].get() == 1:
                self.axes.plot(tspan, self.be.getDictEntry(i))

        # Diese Methode war zunächst eine alternative, die über einen bool abgefragt wurde.
        # Der wesentliche Plot funkioniert auch ohne das Styling.
        self.useStyle()

        # Das finale Zeichnen des aktualisierten Canvas
        self.canvas.draw()

    def useStyle(self):
        """[INFO: ] Styling will remove top and right spines
        of plot and apply vertical lines to visualize single
        years more clearer"""

        # Entfernt die Rahmen an der Figur
        self.figure.gca().spines["top"].set_visible(False)
        self.figure.gca().spines["right"].set_visible(False)

        # Zeichnet vertikale Hilfslinien an jedem "Januar" Eintrag
        i = 0
        while i <= 60:
            self.axes.axvline(i, alpha=0.25, c="gray")
            i += 12

        # Greift auf die Benennung xTicks zu und formatiert sie
        self.axes.set_xticks(self.timespan)
        self.axes.set_xticklabels(self.timespan, rotation=90)
