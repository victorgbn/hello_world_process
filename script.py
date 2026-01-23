import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

def print_numbers_1_to_1000():
    for i in range(1, 1001):
        time.sleep(10)
        logger.info("Counter value: %s", i)

if __name__ == "__main__":
    logger.info("Starting counter...")
    print_numbers_1_to_1000()
    logger.info("Counter finished.")