
# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

print("========== Countdown Generator ==========")

def countdown(n):
    while n > 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)


print("========== Even Numbers Generator ==========")

def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number


print(list(evens(10)))


print("========== File Generator ==========")

# Create a text file with 50 lines
with open("sample_log.txt", "w") as file:
    for number in range(1, 51):
        if number % 10 == 0:
            file.write(f"ERROR: Problem found on line {number}\n")
        else:
            file.write(f"INFO: Normal activity on line {number}\n")


# Read file lines using a generator
def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line


# Return only lines containing ERROR
def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


error_count = 0

for error in only_errors(read_lines("sample_log.txt")):
    print(error.strip())
    error_count += 1

print("Total ERROR lines:", error_count)

print("==========================================")



print("========== Decorators Challenge ==========")

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print("Execution Time:", end - start, "seconds")
        return result

    return wrapper


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Called:", func.__name__)
        result = func(*args, **kwargs)
        return result

    return wrapper


@timer
@log_calls
def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total


print("Sum:", calculate_sum(1000000))

print("==========================================")
