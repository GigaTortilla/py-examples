import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.sampledata.iris import flowers


def main(argv=None) -> int:
    # Beispiel-Daten und Ausgabedatei erzeugen
    x = [1, 2, 3, 4, 5]
    y = [5, 6, 1, 3, 4]
    output_file("line_example.html", title="Bokeh Examples")

    plot = figure(title="Line Plot", x_axis_label="x axis", \
                  y_axis_label="y axis")
    plot.line(x, y, legend="line example", line_width=2)
    show(plot)
    return 0