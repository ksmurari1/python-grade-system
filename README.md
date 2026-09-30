
# Grade System – Python

A simple Python-based grade calculator developed as part of my Social Eagle AI learning journey.

## Project Overview

This project accepts a student's mark as input, validates the input, and assigns a grade based on predefined mark ranges.

## Features

- Accepts numeric marks as user input.
- Handles invalid inputs using `try-except`.
- Validates marks within the range of 0 to 100.
- Assigns grades using conditional statements.
- Handles zero and negative-zero inputs.

## Grade Criteria

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | E |

## Technologies Used

- Python 3.12
- Visual Studio Code
- Python virtual environment (`.venv`)

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:

   ```bash
   py -3.12 -m venv .venv
   ```

   Windows CMD:

   ```cmd
   .venv\Scripts\activate.bat
   ```

4. Run the program:

   ```bash
   python grade_system.py
   ```

5. Enter a mark between 0 and 100 when prompted.

## Sample Output

```text
Please enter a Mark: 95
Your Mark is : 95
Your Grade is: A
```

## Outcomes

- Python variables and data types
- User input and type conversion
- Exception handling using try-except-else
- Conditional statements (if-elif-else)
- Input validation and basic testing

