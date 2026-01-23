import time
def print_numbers_1_to_1000():
    """Print numbers from 1 to 1000 inclusive, one per line."""
    for i in range(1, 1001):
        time.sleep(10)
        print(i)

if __name__ == "__main__":
    print_numbers_1_to_1000()