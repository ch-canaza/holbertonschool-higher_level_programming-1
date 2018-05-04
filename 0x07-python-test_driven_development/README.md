# 0x07. Python - Test-driven development

## OBJECTIVES   
   * how to write Docstrings to create tests   
   * how to write documentation for each module and function   
   * what are the basic option flags to create tests   
   * how to find edge cases   

## REQUIREMENTS   

### PYTHON SCRIPT REQUIREMENTS  
   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   

### PYTHON TEST CASE REQUIREMENTS    
   * all test files should be in the folder `tests`   
   * all test files should be text files (extension: `.txt`)   
   * all test files should be executed using the command `python3 -m doctest ./tests/*`   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all functions (inside and outside of classes) should have documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'`   

## EXERCISES   

### MANDATORY   

**[0-add_integer.py](0-add_integer.py)** - Adds two integers   
Test File: [tests/0-add_integer.txt](tests/0-add_integer.txt)   
Prototype: `def add_integer(a, b=98):`   

**[2-matrix_divided.py](2-matrix_divided.py)** - Divides all elements of a matrix   
Test File: [tests/2-matrix_divided.txt](tests/2-matrix_divided.txt)   
Prototype: `def matrix_divided(matrix, div):`   

**[3-say_my_name.py](3-say_my_name.py)** - Prints "My name is <first name> <last name>"   
Test File: [tests/3-say_my_name.txt](tests/3-say_my_name.txt)   
Prototype: `def say_my_name(first_name, last_name=""):`   

**[4-print_square.py](4-print_square.py)** - Prints a square with the character `#`    
Test File: [tests/4-print_square.txt](tests/4-print_square.txt)   
Prototype: `def print_square(size):`   

**[5-text_indentation.py](5-text_indentation.py)** - Prints text with two new lines after each of these characters: `.`, `?`, and `:`   
Test File: [tests/5-text_indentation.txt](tests/5-text_indentation.txt)   
Prototype: `def text_indentation(text):`   

**[tests/6-max_integer_test.py](tests/6-max_integer_test.py)** - Add unit tests for the function `def max_integer(list=[]):`   

### ADVANCED   

**[100-matrix_mul.py](100-matrix_mul.py)** - Multiplies two matrices    
Test File: [tests/100-matrix_mul.txt](tests/100-matrix_mul.txt)   
Prototype: `def matrix_mul(m_a, m_b):`   

**[101-lazy_matrix_mul.py](101-lazy_matrix_mul.py)** - Multiplies two matrices using the module [NumPy](http://www.numpy.org)    
Test File: [tests/101-lazy_matrix_mul.txt](tests/101-lazy_matrix_mul.txt)   
Prototype: `def lazy_matrix_mul(m_a, m_b):`   

**[102-python.c](102-python.c)** - Prints Python strings   
Prototype: `void print_python_string(PyObject *p);`   
