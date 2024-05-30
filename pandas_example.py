import logging
from example_logs import init_log
import numpy as np
import pandas as pd


def main(argv=None) -> int:
    init_log(logname="pandas")
    logging.info("Logging started.")
    logging.info("NumPy version: " + np.__version__)
    logging.info("Pandas version: " + pd.__version__)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())