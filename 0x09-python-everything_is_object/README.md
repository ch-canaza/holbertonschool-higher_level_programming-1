# 0x09. Python - Everything is object

## OBJECTIVES   
A simple, quiz-like project on:   
   * objects   
   * references   
   * assignments   
   * mutable vs. immutable objects   
   * aliases   
   * variable identifiers   

## REQUIREMENTS   

### PYTHON SCRIPT REQUIREMENTS  
   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all functions (inside and outside of classes) should have documentation   
`python3 -c 'print(__import__("my_module").my_function.__doc__)'`   

### .TXT ANSWER FILE REQUIREMENTS
   * only one line   
   * no shebang   
   * all files should end with a new line   

## EXERCISES   

### MANDATORY   

**[0-answer.txt](0-answer.txt)** - What function would you use to print the type of an object?   

**[1-answer.txt](1-answer.txt)** - What function would you use to to get variable identifier (which is the memory address in the CPython implementation)?   

**[2-answer.txt](2-answer.txt)** - In the following code, do a and b point to the same object? Answer with Yes or No.   
```
>>> a = 89
>>> b = 100
```

**[3-answer.txt](3-answer.txt)** - In the following code, do a and b point to the same object? Answer with Yes or No.   
```
>>> a = 89
>>> b = 89
```

**[4-answer.txt](4-answer.txt)** - In the following code, do a and b point to the same object? Answer with Yes or No.   
```
>>> a = 89
>>> b = a
```

**[5-answer.txt](5-answer.txt)** - In the following code, do a and b point to the same object? Answer with Yes or No.   
```
>>> a = 89
>>> b = a + 1
```

**[6-answer.txt](6-answer.txt)** - What should those 3 lines print?   
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

**[7-answer.txt](7-answer.txt)** - What should those 3 lines print?   
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

**[8-answer.txt](8-answer.txt)** - What should those 3 lines print?   
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

**[9-answer.txt](9-answer.txt)** - What should those 3 lines print?   
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

**[10-answer.txt](10-answer.txt)** - What should those 3 lines print?   
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

**[11-answer.txt](11-answer.txt)** - What should those 3 lines print?   
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

**[12-answer.txt](12-answer.txt)** - What should those 3 lines print?   
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

**[13-answer.txt](13-answer.txt)** - What should those 3 lines print?   
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

**[14-answer.txt](14-answer.txt)** - What should those 3 lines print?   
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

**[15-answer.txt](15-answer.txt)** - What should those 3 lines print?   
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

**[16-answer.txt](16-answer.txt)** - What should those 3 lines print?   
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

**[17-answer.txt](17-answer.txt)** - What should those 3 lines print?   
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

**[18-answer.txt](18-answer.txt)** - What should those 3 lines print?   
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

**[19-copy_list.py](19-copy_list.py)** - Write a function that returns a **copy** of a list    
Prototype: `def copy_list(l):`   

**[20-answer.txt](20-answer.txt)** - Is a a tuple? Answer with Yes or No.   
```
a = ()
```

**[21-answer.txt](21-answer.txt)** - Is a a tuple? Answer with Yes or No.   
```
a = (1, 2)
```

**[22-answer.txt](22-answer.txt)** - Is a a tuple? Answer with Yes or No.   
```
a = (1)
```

**[23-answer.txt](23-answer.txt)** - Is a a tuple? Answer with Yes or No.   
```
a = (1, )
```

**[24-answer.txt](24-answer.txt)** - What should those 3 lines print?   
```
a = (1)
b = (1)
a is b
```

**[25-answer.txt](25-answer.txt)** - What should those 3 lines print?   
```
a = (1, 2)
b = (1, 2)
a is b
```

**[26-answer.txt](26-answer.txt)** - What should those 3 lines print?   
```
a = ()
b = ()
a is b
```

**[27-answer.txt](27-answer.txt)** - Will the last line of this script print 139926795932424? Answer with Yes or No.   
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

**[28-answer.txt](28-answer.txt)** - Will the last line of this script print 139926795932424? Answer with Yes or No.   
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

**Blog Post: [Python Objects](https://medium.com/@lizzie_turner/python-objects-cac2c73b1bec)** - Write a blog post on everything this project covers. It should be organized in the following way:   
	* Introduction   
	* ID and Types   
	* Mutable objects   
	* Immutable objects   
	* How differently does Python treat mutable and immutable objects and why does it matter?   
	* How are arguments passed to functions? What does that imply for mutable and immutable objects?   

### ADVANCED   

**[100-magic_string.py](100-magic_string.py)** - Write a function `magic_string()` that returns a string "Holberton" n times the number of iterations.    

**[101-locked_class.py](101-locked_class.py)** - Write a class `LockedClass` with no class or object attribute, that prevents the user to dynamically create new instance attributes, except if the new instance attribute is called `first_name`.   

**103-line**   
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:   
   * [103-line1.txt](103-line1.txt) - How many int objects are created by the execution of the first line of the script?   
   * [103-line2.txt](103-line2.txt) - How many int objects are created by the execution of the second line of the script?   

**104-line**   
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:   
   * [104-line1.txt](104-line1.txt) - How many int objects are created by the execution of the first line of the script?   
   * [104-line2.txt](104-line2.txt) - How many int objects are created by the execution of the second line of the script   
   * [104-line3.txt](104-line3.txt) - After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No   
   * [104-line4.txt](104-line4.txt) - After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No   
   * [104-line5.txt](104-line5.txt) - How many int objects are created by the execution of the last line of the script   

**105-line** -   
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:   
   * [105-line1.txt](105-line1.txt) - Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory?   
