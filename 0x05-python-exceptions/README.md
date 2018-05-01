# 0x05. Python - Exceptions   

## OBJECTIVES   
   * the differences between errors and exceptions
   * how, when, and why to use exceptions
   * how to raise a builtin exception
   * how to implement a clean-up action after an exception
   * how to use `try: / except: / finally:`

## REQUIREMENTS   

   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   

## EXERCISES   

### MANDATORY   

**[0-safe_print_list.py](0-safe_print_list.py)** - Prints `x` elements of a list   
Prototype: `def safe_print_list(my_list=[], x=0):`   

**[1-safe_print_integer.py](1-safe_print_integer.py)** - Prints an integer with `"{:d}".format()`   
Prototype: `def safe_print_integer(value):`   

**[2-safe_print_list_integers.py](2-safe_print_list_integers.py)** - Prints the first `x` integer elements of a list    
Prototype: `def safe_print_list_integers(my_list=[], x=0):`   

**[3-safe_print_division.py](3-safe_print_division.py)** - Divides two functions and prints the result   
Prototype: `def safe_print_division(a, b):`   

**[4-list_division.py](4-list_division.py)** - Divides two lists element by element   
Prototype: `def list_division(my_list_1, my_list_2, list_length):`  

**[5-raise_exception.py](5-raise_exception.py)** - Raises a type exception   
Prototype: `def raise_exception():`  

**[6-raise_exception_msg.py]( 6-raise_exception_msg.py)** - Raises a name exception with a message   
Prototype: `def raise_exception_msg(message=""):`  

### ADVANCED   

**[def raise_exception_msg(message=\"\"):](def raise_exception_msg(message=\"\"):)** - Prints an integer    
Prototype: `def safe_print_integer_err(value):`  

**[101-safe_function.py](101-safe_function.py)** - Executes a function safely   
Prototype: `def safe_function(fct, *args):`  

**[102-magic_calculation.py](102-magic_calculation.py)** - Does exactly the same as the following Python bytecode   
Prototype: `def magic_calculation(a, b):`  
```
3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```

**[103-python.c](103-python.c)** - Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
Prototypes: `void print_python_list(PyObject *p);`, `void print_python_bytes(PyObject *p);`, `void print_python_float(PyObject *p);`   
