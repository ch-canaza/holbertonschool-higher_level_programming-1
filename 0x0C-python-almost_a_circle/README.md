# 0x0C. Python - Almost a circle

## OBJECTIVES   
Review the following Python concepts:   
   * import   
   * exceptions   
   * classes   
   * private, protected, and public attributes   
   * getter/setter   
   * class, static, and public methods   
   * inheritance   
   * unittests   
   * file i/o   
Learn the following new concepts:   
   * `args` and `kwargs`   
   * serialization and deserialization   
   * JSON   

## REQUIREMENTS   

### PYTHON SCRIPT REQUIREMENTS  
   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all functions (inside and outside of classes) should have documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'`   

### PYTHON UNIT TEST REQUIREMENTS
   * all test files should be in the folder `tests`   
   * tests must use the [unittest module](https://intranet.hbtn.io/rltoken/T7uxwxtGdbRRW9pkD4eO0g)   
   * all test files should start with `test_`   
   * all test files should execute with the command `python3 -m unittest discover tests`   
   * files can also be tested with the command `python3 -m unittest tests/test_models/test_base.py`   

## FILE STRUCTURE   

**[models](models)**   
   * [\__init_\_.py](models/__init__.py) - initialization file to turn folder into a Python module   
   * [base.py](models/base.py) - contains the class Base   
   * [rectangle.py](models/rectangle.py) - contains the class Rectangle   
   * [square.py](models/square.py) - contains the class Square   

**[tests/test_models](tests/test_models)**   
   * [test_models/base.py](tests/test_models/base.py) - test files related to class Base   
   * [test_models/rectangle.py](tests/test_models/rectangle.py) - tests files related to class Rectangle   
   * [test_models/square.py](tests/test_models/square.py) - test files related to class Square   