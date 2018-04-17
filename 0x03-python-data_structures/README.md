# 0x03. Python - Data Structures: Lists, Tuples  

## OBJECTIVES   
   * What are lists and how to use them
   * What are the differences and similarities between strings and lists
   * What are the most common methods of lists and how to use them
   * How to use lists as stacks and queues
   * What are list comprehensions and how to use them
   * What are tuples and how to use them
   * When to use tuples versus lists
   * What is a sequence
   * What is tuple packing
   * What is sequence unpacking
   * What is the del statement and how to use it

## REQUIREMENTS   

### PYTHON REQUIREMENTS  
   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   

### C REQUIREMENTS  
   * all files will be compiled on Ubuntu 14.04 LTS
   * files will be compiled with `gcc 4.8.4` using the flags `-Wall` `-Wextra` `-Werror` and `-pedantic`
   * all code should use the `Betty` style
   * no more than 5 functions per file

## EXERCISES   

### MANDATORY   
**[0-print_list_integer.py](0-print_list_integer.py)** -  Print a list of integers    
Prototype: `def print_list_integer(my_list=[]):`   

**[1-element_at.py](1-element_at.py)** - Print an element at a certain position in a list     
Prototype: `def element_at(my_list, idx):`   

**[2-replace_in_list.py](2-replace_in_list.py)** - Write a function that replaces an element of a list at a specific position   
Prototype: `def replace_in_list(my_list, idx, element):`

**[3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)** - Print a list of integers in reverse   
Prototype: `def print_reversed_list_integer(my_list=[]):`

**[4-new_in_list.py](4-new_in_list.py)** - Replace an element in a list at a specific position without modifying the original list  
Prototype: `def new_in_list(my_list, idx, element):`

**[5-no_c.py](5-no_c.py)** - Remove all characters `c` and `C` from a string   
Prototype: `def no_c(my_string):`

**[6-print_matrix_integer.py](6-print_matrix_integer.py)** - Print a matrix of integers  
Prototype: `def print_matrix_integer(matrix=[[]]):`

**[7-add_tuple.py](7-add_tuple.py)** - Adds 2 tuples   
Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`

**[8-multiple_returns.py](8-multiple_returns.py)** - Returns a tuple with the length of a string and its first character.  
Prototype: `def multiple_returns(sentence):`

**[9-max_integer.py](9-max_integer.py)** -  Find the biggest integer in a list  
Prototype: `def max_integer(my_list=[]):`

**[10-divisible_by_2.py](10-divisible_by_2.py)** - Find all multiples of 2 in a list  
Prototype: `def divisible_by_2(my_list=[]):`

**[11-delete_at.py](11-delete_at.py)** - Deletes the item at a specific position in a list   
Prototype: `def delete_at(my_list=[], idx=0):`

**[12-switch.py](12-switch.py)** - Complete the [source code](https://intranet.hbtn.io/rltoken/RfHRsVZK5IVZ5e4-0WAOJQ) to switch the value of `a` and `b`

**[13-is_palindrome.c](13-is_palindrome.c)** - Write a function in C that checks if a singly linked list is a palindrome. Include a guarded header file named `lists.h` containing all prototypes.
Prototype: `int is_palindrome(listint_t **head);`


### ADVANCED   

**[100-print_python_list_info.c](100-print_python_list_info.c)** - Create a C function that prints some basic info about Python lists.  
The shared library will be compiled with the following command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`  
Prototype: `void print_python_list_info(PyObject *p);`
