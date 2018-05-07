# 0x08. Python - More Classes and Objects   

## OBJECTIVES   
An intermediate project focusing on:   
   * objects   
   * attributes   
   * the `__init__` method   
   * the `__str__` and `__repr__` methods   
   * data abstraction, data encapsulation, and information hiding   
   * public-, protected-, and private- attributes   
   * destructor   

## REQUIREMENTS   

   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all classes should have documentation `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`   
   * all functions (inside and outside of classes) should have documentation   
`python3 -c 'print(__import__("my_module").my_function.__doc__)' and`   
`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`   


## EXERCISES   

### MANDATORY   

**[0-rectangle.py](0-rectangle.py)** - create class `Rectangle` that defines a rectangle   

**[1-rectangle.py](1-rectangle.py)** - Empty class `Rectangle` with:   
* private instance attribute `width`   
  * property `def width(self):` to retrieve it   
  * property setter `def width(self, value):` to set it   
* private instance attribute `height`   
  * property `ef height(self):` to retrieve it   
  * property setter `def height(self, value):` to set it   
* instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`   

**[2-rectangle.py](2-rectangle.py)** - class `Rectangle` with all of the above and:   
* public instance method `def area(self):` that returns the rectangle's area   
* public instance method `def perimeter(self):` that returns the rectangle's perimeter   

**[3-rectangle.py](3-rectangle.py)** - class `Rectangle` with all of the above and:   
* `print()` and `str()` should print the rectangle with the character `#`   

**[4-rectangle.py](4-rectangle.py)** - class `Rectangle` with all of the above and:   
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`   

**[5-rectangle.py](5-rectangle.py)** - class `Rectangle` with all of the above and:   
* prints the message `Bye rectangle...` when an instance of `Rectangle` is deleted   

**[6-rectangle.py](6-rectangle.py)** - class `Rectangle` with all of the above and:   
* public class attribute `number_of_instances`:   
  * initialized to 0   
  * incremented during new instance initialization   
  * decremented during instance deletion   

**[7-rectangle.py](7-rectangle.py)** - class `Rectangle` with all of the above and:   
* public class attribute `print_symbol`:   
  * initialized as `#`   
  * can be any symbol and any type   

**[8-rectangle.py](8-rectangle.py)** - class `Rectangle` with all of the above and:   
* static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on area   

**[9-rectangle.py](9-rectangle.py)** - class `Rectangle` with all of the above and:   
* class method `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`   

### ADVANCED   

**[Blog Post](www.google.com)** - Write a blog post describing how object and class attributes work   
* What’s a class attribute   
* What’s an instance attribute   
* What are all the way to create them and what is the Pythonic way of doing it   
* What are the differences between class and instance attributes   
* What are the advantages and drawbacks of each of them   
* How does Python deal with the object and class attributes using the `__dic__`   


**[101-nqueens.py](101-nqueens.py)** - Solve the N queens puzzle    
Usage: `nqueens N`   
