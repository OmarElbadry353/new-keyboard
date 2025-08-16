import os
from collections import deque

def receivedText(s):
    left_part = deque()  # Characters to the left of the cursor
    right_part = deque() # Characters to the right of the cursor
    numeric_lock_on = True # Initial state: numeric lock is on

    for char in s:
        if char == '<':  # Home key
            while left_part:
                right_part.appendleft(left_part.pop())
        elif char == '>':  # End key
            while right_part:
                left_part.append(right_part.popleft())
        elif char == '*':  # Backspace key
            if left_part:
                left_part.pop()
        elif char == '#':  # Numeric Lock key
            numeric_lock_on = not numeric_lock_on
        elif '0' <= char <= '9': # Digits
            if numeric_lock_on:
                left_part.append(char)
        else:  # Latin letters, underscores, other symbols
            left_part.append(char)

    return "".join(left_part) + "".join(right_part)

if __name__ == '__main__':
    # Check if 'OUTPUT_PATH' environment variable is set
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        S = input()
        result = receivedText(S)
        fptr.write(result + '\n')
        fptr.close()
    else:
        # If 'OUTPUT_PATH' is not set (e.g., during local development),
        # print directly to console or a default file.
        # For simplicity, let's print to console for local testing.
        S = input("Enter text: ") # Add a prompt for better user experience
        result = receivedText(S)
        print(result) # Print to standard output (console)