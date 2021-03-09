#### Hier kommt alles rein, was mit dem Plotten zu tun hat.
import matplotlib.pyplot as plt

def plotFigure(tspan, selectedList, styling):

    plt.figure(figsize=(15, 5))
    plt.title("Auswahl")

    if styling:
        useStyle()

    plt.xticks(rotation=90, size=8)
    plt.plot(tspan, selectedList)
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