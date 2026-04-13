import time
import logging
import os
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

def print_env_varibales():
    logger.info("Environment Variables :")
    print("s3 values")
    print(os.environ.get("S3_ACCESS_KEY_ID"))

    print("Copernicus Marine values :")
    print(os.environ.get("COPERNICUSMARINE_SERVICE_USERNAME"))
    print(os.environ.get("COPERNICUSMARINE_SERVICE_PASSWORD"))

    print("Others :")
    for key, value in os.environ.items():
        if key not in ["S3_ACCESS_KEY_ID", "S3_SECRET_ACCESS_KEY", "COPERNICUSMARINE_SERVICE_USERNAME", "COPERNICUSMARINE_SERVICE_PASSWORD"]:
            print("%s: %s", key, value)

def print_numbers_1_to_1000():
    for i in range(1, 1001):
        time.sleep(10)
        logger.info("Counter value: %s", i)

if __name__ == "__main__":
    logger.info("Starting counter...")
    print_env_varibales()
    # print_numbers_1_to_1000()
    logger.info("Counter finished.")