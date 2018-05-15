# 0x0A. Python - Inheritance   

## OBJECTIVES   
Be able to explain:   
   * superclasses, baseclasses, parentclasses, and subclasses   
   * inheritance   
   * the builtin functions `isinstance`, `issubclass`, `type`, and `super`   

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

**[0-lookup.py](0-lookup.py)** - Write a function that returns the list of available attributes and methods of an object   
Prototype: `def lookup(obj):`   

**[1-my_list.py](1-my_list.py)** - Write a class `MyList` that inherits from `list`   
   * Public Instance Method: `def print_sorted(self):`    

Test Files: [tests/1-my_list.txt](tests/1-my_list.txt)   

**[2-is_same_class.py](2-is_same_class.py)** - Write a function that returns `True` if the object is an instance of the specified class and `False` otherwise   
Prototype: `def is_same_class(obj, a_class):`   

**[3-is_kind_of_class.py](3-is_kind_of_class.py)** - Write a function that returns `True` if the object is an instance of the specified class or a class that inherited from that clase and `False` otherwise   
Prototype: `def is_kind_of_class(obj, a_class):`   

**[4-inherits_from.py](4-inherits_from.py)** - Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class and `False` otherwise   
Prototype: `def inherits_from(obj, a_class):`   

**[5-base_geometry.py](5-base_geometry.py)** - Write an empty class `BaseGeometry`   

**[6-base_geometry.py](6-base_geometry.py)** - Write a class BaseGeometry   
   * Public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`   

**[7-base_geometry.py](7-base_geometry.py)** - Write a class `BaseGeometry` with all of the above and:   
   * Public instance method `def integer_validator(self, name, value):` that validates `value`   
      * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`   
      * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`   

Test Files: [tests/7-base_geometry.txt](tests/7-base_geometry.txt)   

**[8-rectangle.py](8-rectangle.py)** - Write a class `Rectangle` that inherits from `BaseGeometry`   
   * Instantiation with `width` and `height`: `def __init__(self, width, height):`   
      * `width` and `height` must be private (no getter or setter)   
      * `width` and `height` must be positive integers, validated by `integer_validator`   

**[9-rectangle.py](9-rectangle.py)** - Write a class `Rectangle` with all of the above and:   
   * the `area()` method must be implemented   
   * `print()` should print and `str()` should return the rectangle description `[Rectangle] <width>/<height>`   

**[10-square.py](10-square.py)** - Write a class `Square` that inherits from `Rectangle`   
   * Instantiation with `size`: `def __init__(self, size):`:   
      * `size` must be private (no getter or setter)   
      * `size` must be a positive integer, validated by `integer_validator`   
   * the `area()` method must be implemented   

**[11-square.py](11-square.py)** - Write a class `Square` with all of the above and:   
   * `print()` should print and `str()` should return the square description `[Square] <width>/<height>`   

### ADVANCED   

**[100-my_int.py](100-my_int.py)** - Write a class `MyInt` that inherits from `int`   
   * `MyInt` has the `==` and `!=` operators reversed   

**[101-add_attribute.py](101-add_attribute.py)** - Write a function that adds a new attribute to an object if it’s possible:   
   * Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute   
