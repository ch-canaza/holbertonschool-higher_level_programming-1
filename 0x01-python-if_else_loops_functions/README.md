This project consists of Python and shell scripts pertaining to if/else statements, loops, and functions in the Python language.

MANDATORY:

0. Complete the [source code](https://intranet.hbtn.io/rltoken/2S3G4vOnRrWymCjKYd6Wew) to determine whether the value stored in variable `number` is positive or negative
1. Complete the [source code](https://intranet.hbtn.io/rltoken/e9k9---MJXcMmIjlMdlBpw) to print the last digit of `number`
2. Write a program that prints the lowercase alphabet not followed by a new line
3. Write a program that prints the lowercase alphabet, except for `q` and `e`, not followed by a new line
4. Write a program that prints all numbers from `0` to `98` in decimal and hexadecimal
5. Write a program that prints all numbers from `0` to `98` in the following format:
```
>>> 00, 01, 02, 03, 04, 05
```
6. Write a program that prints all possible combinations of two digits
7. Write a function that checks for a lowercase character:
   * returns `True` if `c` is lowercase
   * returns `False` otherwise
8. Write a function that prints a string in uppercase, followed by a new line
9. Write a function that prints the last digit of a number
10. Write a function that adds two integers and returns the result
11. Write a function that computes `a` to the power of `b` and return the value
12. FizzBuzz
13. Write a C function that inserts a number into a sorted singly linked list

ADVANCED:

14. Write a program that prints the alphabet, in reverse order, alternating lowercase and uppercase (i.e. `z` in lowercase and `Y` in uppercase), not followed by a new line
15. Write a function that creates a copy of the string, removing the character at position `n`
16. Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```