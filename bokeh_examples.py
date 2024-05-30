import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers


def main(argv=None) -> int:
    # Beispiel-Daten und Ausgabedatei erzeugen
    x = [1, 2, 3, 4, 5]
    y = [5, 6, 1, 3, 4]
    output_file("line_example.html")
    return 0