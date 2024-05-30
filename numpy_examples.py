import numpy as np
import logging
from example_logs import init_log


def main(argv=None) -> int:
    init_log()
    logging.info("Logging started. NumPy version: " + np.__version__)

    my_list = list(range(0, 6))
    my_array = np.array(my_list)
    logging.debug("List object converted to NumPy-Array: " + my_array)

    if isinstance(my_array, np.ndarray):
        logging.debug("The variable my_array is a NumPy-Array.")

    # Arrays können auch mehrdimensionale Strukturen abbilden
    my_array_2 = np.array(list(range(0,11))).reshape(5, 2)
    logging.debug("1D-Array: " + my_array + "\n2D-Array: " + my_array_2)

    # Array Eigenschaften
    logging.debug("Datentyp: " + my_array_2.dtype)
    logging.debug("Dimension: " + my_array_2.ndim)
    logging.debug("Anzahl der Elemente: " + my_array_2.size)
    logging.debug("Bytes pro Element: " + my_array_2.itemsize)
    logging.debug("Ort im Arbeitsspeicher: " + my_array_2.data)

    # Beim Mischen von Datentypen wird Konsistenz erzwungen
    # Hier werden alle Zahlen zu Strings konvertiert, 
    # da Arrays nur einen Datentyp erlauben
    my_array_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, "neun"]])
    logging.debug("Array Konsistenz hergestellt... " + my_array_3)

    arr_1 = np.array([1, 9, 7, 2])
    arr_2 = np.array([1, 4, 2, 2])
    logging.debug("Elementweise Addition: " + (arr_1 + arr_2))
    logging.debug("Elementweise Subtraktion: " + (arr_1 - arr_2))
    logging.debug("Elementweise Multiplikation: " + (arr_1 * arr_2))
    logging.debug("Elementweise Division: " + (arr_1 / arr_2))



# Example code to showcase logging functionality
if __name__ == '__main__':
    raise SystemExit(main())