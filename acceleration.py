from numba import jit
from time import process_time
import numpy as np


# jit-Dekorator gibt an, dass Code Just-in-Time kompiliert wird
# Code läuft damit in nur 3 % der ursprünglich nötigen Zeitdauer
@jit(nopython=True)
def sum2dimensional(np_array: np.ndarray):
    array_rows, array_cols = np_array.shape
    result = 0.0
    for i in range(array_rows):
        for j in range(array_cols):
            result += np_array[i, j]
    return result


def main(argv=None):
    start_time = process_time()

    np_array = np.arange(100000000).reshape(10000, 10000)
    print(sum2dimensional(np_array))

    end_time = process_time()
    print("Process duration: " + str(end_time - start_time))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
