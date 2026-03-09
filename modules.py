import os
import math

print(f"Current working directory: {os.getcwd()}")

num = int(input("Enter an integer: "))
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

print(f"Floor: {math.floor(log_val)}")
print(f"Ceiling: {math.ceil(log_val)}")
