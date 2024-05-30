import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


def main(argv=None):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Einfache Diagramme
    style.use('ggplot')
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].plot(x, y, label="line plot example", linewidth=2)
    ax[0, 0].legend()
    ax[0, 0].grid(True, color="k")
    ax[0, 0].set_ylabel("y axis")
    ax[0, 0].set_xlabel("x axis")
    ax[0, 0].set_title("Line Plot")
    ax[0, 1].barh(x, y, label="horizontal bar chart example", linewidth=2)
    ax[0, 1].legend()
    ax[0, 1].grid(True, color="k")
    ax[0, 1].set_ylabel("y axis")
    ax[0, 1].set_xlabel("x axis")
    ax[0, 1].set_title("Horizontal Bar Chart")
    ax[1, 0].bar(x, y, label="bar chart example", linewidth=2)
    ax[1, 0].legend()
    ax[1, 0].grid(True, color="k")
    ax[1, 0].set_ylabel("y axis")
    ax[1, 0].set_xlabel("x axis")
    ax[1, 0].set_title("Vertical Bar Chart")
    ax[1, 1].scatter(x, y, label="scatter plot example", linewidth=2)
    ax[1, 1].legend()
    ax[1, 1].grid(True, color="k")
    ax[1, 1].set_ylabel("y axis")
    ax[1, 1].set_xlabel("x axis")
    ax[1, 1].set_title("Scatter Plot")
    plt.show()

    # Histogramm erzeugen
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(10000)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(x, bins=50, density=True, facecolor='r', alpha=0.75, \
            label='Histogram Plot Example')
    # $math_text$ formatiert Text zu mathematischen Ausdrücken
    ax.text(45, 0.028, r'$\mu=100,\ \sigma=15$')
    ax.axis([40, 160, 0, 0.03])
    plt.legend()
    plt.grid(True, color="k")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.title("Histogram Plot")
    plt.show()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())