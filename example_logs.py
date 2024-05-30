import logging
import time


def init_log_dbg() -> None:
    start_time = time.localtime()
    logging.basicConfig(filename="logs/"+"-".join(start_time[0:3])+"_"+":".join(start_time[3:5])+".log", \
                        filemode="w", level=logging.DEBUG, \
                        format="%(asctime)s - %(levelname)s::%(module)s::%(funcName)s at line %(lineno)d - %(message)s")


def main(argv=None) -> int:
    pass


# Example code to showcase logging functionality
if __name__ == '__main__':
    raise SystemExit(main())