import logging
import time


def init_log(logname: str = "example",
             loglevel: int = logging.DEBUG) -> None:
    start_time = time.localtime()
    logging.basicConfig(filename="logs/" +
                        "-".join([str(i) for i in start_time[0:3]]) + "_"
                        + str.format("{:02}-{:02}", start_time.tm_hour, start_time.tm_min)
                        + "_" + logname + ".log", filemode="w", level=loglevel,
                        format="%(asctime)s - %(levelname)s::%(module)s::"
                        + "%(funcName)s at line %(lineno)d - %(message)s")


def main(argv=None) -> int:
    pass


# Example code to showcase logging functionality
if __name__ == '__main__':
    raise SystemExit(main())
