# New Keyboard

## Overview
This project solves the "New Keyboard" problem, which simulates the behavior of a highly idiosyncratic keyboard. The keyboard features special keys like Numeric Lock, Home, End, and Backspace, each with unique text manipulation functionalities. The problem requires processing a sequence of key presses from an input string and accurately determining the final text that would appear. It's a challenge in string manipulation and algorithm design, particularly focusing on efficient dynamic cursor management.

## How to Run
```bash
python src/main.py
```

## How to Run Tests with Coverage
```bash
python -m pytest --cov=src.main --cov-branch --cov-report=term-missing test.py
```

## Expected Output
Upon successful execution, the program will output a single line of text to standard output (the console). This line will represent the final string that results from processing all the key presses defined in the input string S, accounting for all the special keyboard functionalities (numeric lock, home, end, and backspace).
