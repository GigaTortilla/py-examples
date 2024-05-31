import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.sampledata.iris import flowers


def main(argv=None) -> int:
    # Beispiel-Daten und Ausgabedatei erzeugen
    x = [1, 2, 3, 4, 5]
    y = [5, 6, 1, 3, 4]
    output_file("line_example.html", title="Bokeh Examples")

    plot = figure(title="Line Plot", x_axis_label="x axis",
                  y_axis_label="y axis")
    plot.line(x, y, legend_label="line example", line_width=2)
    show(plot)

    x = np.linspace(-6, 6, 100)
    y = np.cos(x)
    output_file("cosx_example.html", title="Scatter Plot")

    plot = figure(title="cos(x) Plot", width=500, height=500,
                  x_axis_label="x axis", y_axis_label="y axis")
    plot.circle(x=x, y=y, size=7, color="firebrick",
                alpha=0.5, legend_label="line example")
    show(plot)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
