# A program that prints hello world
print("hello world")
import time
import sys

# ANSI color codes for rainbow colors
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]

reset = "\033[0m"

message = "Hello, World!"

# Print each character in rainbow colors with a delay
for i, char in enumerate(message):
    color = colors[i % len(colors)]  # cycle through colors
    sys.stdout.write(color + char + reset)
    sys.stdout.flush()
    time.sleep(0.2)  # delay for animation

print("\n")  # move to next line

# Bonus: print the whole message multiple times in different colors
for color in colors:
    print(color + message + reset)
    time.sleep(0.3)