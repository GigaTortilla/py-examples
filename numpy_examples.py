import numpy as np
import logging
from example_logs import init_log


def main(argv=None) -> int:
    init_log()
    logging.info("Logging started. NumPy version: " + np.__version__)

    my_list = list(range(0, 6))
    my_array = np.array(my_list)
    logging.debug("List object converted to NumPy-Array: " + str(my_array))

    if isinstance(my_array, np.ndarray):
        logging.debug("The variable my_array is a NumPy-Array.")

    # Arrays können auch mehrdimensionale Strukturen abbilden
    my_array_2 = np.array(list(range(1, 11))).reshape(5, 2)
    logging.debug("1D-Array: " + str(my_array)
                  + "\n2D-Array: " + str(my_array_2))

    # Array Eigenschaften
    logging.debug("Datentyp: " + str(my_array_2.dtype))
    logging.debug("Dimension: " + str(my_array_2.ndim))
    logging.debug("Anzahl der Elemente: " + str(my_array_2.size))
    logging.debug("Bytes pro Element: " + str(my_array_2.itemsize))
    logging.debug("Ort im Arbeitsspeicher: " + str(my_array_2.data))

    # Beim Mischen von Datentypen wird Konsistenz erzwungen
    # Hier werden alle Zahlen zu Strings konvertiert, 
    # da Arrays nur einen Datentyp erlauben
    my_array_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, "neun"]])
    logging.debug("Array Konsistenz hergestellt... " + str(my_array_3))

    arr_1 = np.array([1, 9, 7, 2])
    arr_2 = np.array([1, 4, 2, 2])
    logging.debug("Elementweise Addition: " + str(arr_1 + arr_2))
    logging.debug("Elementweise Subtraktion: " + str(arr_1 - arr_2))
    logging.debug("Elementweise Multiplikation: " + str(arr_1 * arr_2))
    logging.debug("Elementweise Division: " + str(arr_1 / arr_2))

    # Statistische Berechnungen mit NumPy
    logging.debug("Median: " + str(np.median(arr_1)))
    logging.debug("Standardabweichung: " + str(np.std(arr_1)))
    logging.debug("Varianz: " + str(np.var(arr_1)))
    logging.debug("Maximaler Wert: " + str(np.max(arr_1)))
    logging.debug("Minimaler Wert: " + str(np.min(arr_1)))
    logging.debug("Summe aller Werte größer als das arithmetische Mittel: "
                  + str(np.sum(arr_1 > np.mean(arr_1))))
    
    my_array_4 = np.random.randn(5)
    logging.debug("Zufallsgeneriertes Array: " + str(my_array_4))

    logging.shutdown()
    return 0


# Example code to showcase logging functionality
if __name__ == '__main__':
    raise SystemExit(main())
