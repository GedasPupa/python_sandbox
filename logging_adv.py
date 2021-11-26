import logging


def main_0():

    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w")

    logging.debug("debug-level message")  # Diagnostic information useful for debugging.
    logging.info("info-level message")  # General information about program execution results.
    logging.warning("warning-level message")  # Something unexpected, or an approaching problem.
    logging.error("error-level message")  # Unable to perform a specific operation due to problem.
    logging.critical("critical-level message")  # Program may not be able to continue, serious error.

    logging.info("Here is a variable '{}' and an int: {}.".format("string", 10))


extraData = {
    "user": "joe@example.com"
}

def anotherFunction():
    logging.debug("This is debug-level message.", extra=extraData)

def main_1():

    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d / %(message)s"
    datestr = "%Y/%m/%d %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is info-level message.", extra=extraData)
    logging.warning("This is warning-level message.", extra=extraData)
    anotherFunction()


if __name__ == "__main__":
    # main_0()
    main_1()