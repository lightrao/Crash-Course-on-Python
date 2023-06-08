import logging
import math

# create and configure logger
LOG_FORMAT = "%(levelname)s:%(name)s:%(asctime)s:%(message)s"
logging.basicConfig(filename="./lumberjack.log", level=logging.NOTSET, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

# Test the logger
# print(logger.level)
# logger.info("Our first message.")

# Test messages
# print(logger.level)
# logger.debug("This is a harmless debug message.")
# logger.info("Just some useful info.")
# logger.warning("Something unexpected has happened.")
# logger.error("An error has occurred, software was unable to perform some function.")
# logger.critical("A serious error has occurred, program itself may shut down.")

def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c = 0"""
    logger.info(f"quadratic_fomula({a},{b},{c})")

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc=b**2-4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1=(-b+math.sqrt(disc))/(2*a)
    root2=(-b-math.sqrt(disc))/(2*a)

    # Return the two roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots=quadratic_formula(1,0,1)
print(roots)
# roots2=quadratic_formula(1,0,-4)
# print(roots2)
# print(math.sqrt(-4))


