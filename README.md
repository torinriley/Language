# Pulse Code

## Overview
Pulse Code is a simple interpreted language designed for educational purposes and basic scripting tasks. It supports fundamental programming constructs such as variable assignment, loops, conditional execution, type casting, and printing.

## Features
- **Variable Assignment**: Assign values to variables.
- **Loops**: `for` loops with a specified range and `until` loops with a condition.
- **Conditional Execution**: Execute blocks of code based on conditions.
- **Type Casting**: Cast variables to different types (`int`, `str`, `bool`, `float`).
- **Printing**: Output values to the console.

## Example Code
```plaintext
x = 0
for i in 1 3
    for j in 1 2
        print i
        print j
    end
end
until x > 5
    print "Looping until x > 5"
    x = x + 1
end
@int x
print x