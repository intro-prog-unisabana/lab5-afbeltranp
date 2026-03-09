from utils import *

message = input("Please type your message\n")
encoded = flip(message) + str(count_letters(message, 'a'))
print(f"Your encoded message is: {encoded}")
