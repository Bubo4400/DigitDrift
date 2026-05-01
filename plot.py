from multiprocessing import Process
import matplotlib.pyplot as plt

def drawPlot(data: dict) -> None:
    keys = sorted(data.keys(), key=lambda x: int(x))
    values = [data[k] for k in keys]

    yVals = keys[::-1]
    xVals = values[::-1]

    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    positions = [i + 1 for i in range(len(yVals))]
    bars = ax.barh(positions, xVals, color="royalblue")
    ax.set_xlim(0, 100)

    ax.set_yticks(positions)
    ax.set_yticklabels(yVals)

    ax.set_title("Frequency of Leading Digits")
    ax.set_xlabel("Frequency of digits (%)")
    ax.set_ylabel("Leading digits")

    for bar, value in zip(bars, xVals):
        x = bar.get_width()
        y = bar.get_y() + bar.get_height() / 2
        ax.text(x + 1, y, f"{value}", va="center", ha="left", color="white")

    plt.tight_layout()
    plt.show()

def processPlot(data):
    p = Process(target=drawPlot, args=(data,)) 
    p.start()
