# 0x06. Python - Classes and Objects   

## OBJECTIVES   
An introduction to:   
   * classes   
   * objects   
   * attributes   
   * the `__init__` method and how to use it   
   * documentation using docstrings   

## REQUIREMENTS   

   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all classes should have documentation `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`   
   * all functions (inside and outside of classes) should have documentation   
`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and   
`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`   

## EXERCISES   

### MANDATORY   

**[0-square.py](0-square.py)** - Empty class `Square` that defines a square   

**[1-square.py](1-square.py)** - Empty class `Square` with:  
* validated private instance attribute: `size`  
* instantiation with `size` (no type/value verification)   

**[2-square.py](2-square.py)** - Empty class `Square` with:   
* validated private instance attribute `size`   
* instantiation with optional `size: def __init__(self, size=0):`   

**[2-square.py](2-square.py)** - Empty class `Square` with:   
* validated private instance attribute `size`   
* instantiation with optional `size: def __init__(self, size=0):`   
* public instance method: `def area(self):` that returns the current square area   

**[4-square.py](4-square.py)** - Empty class `Square` with:   
* validated private instance attribute `size`   
* property `def size(self):` to retrieve it   
* property setter `def size(self, value):` to set it:   

**[5-square.py](5-square.py)** - Empty class `Square` with:   
* validated private instance attribute `size`   
* instantiation with optional size: `def __init__(self, size=0):`   
* public instance method: `def area(self):` that returns the current square area   
* public instance method: `def my_print(self):` that prints in stdout the square with the character `#`   

**[6-square.py](6-square.py)** - Empty class `Square` with:   
* validated private instance attribute `size`   
  * property `def size(self):` to retrieve it   
  * property setter `def size(self, value):` to set it   
* validated private instance attribute: `position:`   
  * property `def position(self):` to retrieve it   
  * property setter `def position(self, value):` to set it   
* public instance method: `def area(self):` that returns the current square area   
* public instance method: `def my_print(self):` that prints in stdout the square with the character `#`   

### ADVANCED   

**[100-singly_linked_list.py](100-singly_linked_list.py)** -    
* Class `Node` that defines a node of a singly linked list by:   
  * private instance attribute `data`   
    * property `def data(self):` to retrieve it   
    * property setter `def data(self, value):` to set it   
  * private instance attribute `next_node`   
    * property `def next_node(self)` to retrieve it   
    * property setter `def next_node(self, value):` to set it   
* Class `SinglyLinkedList` that defines a singly linked list by:   
  * private instance attribute `head` (no setter or getter)   
  * simple instantiation: `def __init__(self):`   
  * public instance method: `def sorted_insert(self, value):` that inserts a new `Node` in the list   

**[101-square.py](101-square.py)** - makes printing a `Square` have the same behavior as `my_print()`   

**[102-square.py](102-square.py)** - add comparision functionality to `Square` class, using comparators `==`, `!=`, `>`, `<`, `>=`, and `<=`   

**[103-magic_class.py](103-magic_class.py)** - Class `MagicClass` that does exactly the same as the following Python bytecode:   
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```