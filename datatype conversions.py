Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(8)
8
>>> int(3.1)
3
>>> int("Meghana")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Meghana")
ValueError: invalid literal for int() with base 10: 'Meghana'
>>> int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(4)
4.0
>>> float(8.9)
8.9
>>> float("hi")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
>>> float(True)
1.0
>>> float(False)
0.0
>>> float(3+9j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> #string
>>> str(8)
'8'
>>> str(6.9)
'6.9'
>>> str("hi")
'hi'
str(9+8j)
'(9+8j)'
str(True)
'True'
str(False)
'False'
#complex
complex(6)
(6+0j)
complex(7.8)
(7.8+0j)
compex("hi")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    compex("hi")
NameError: name 'compex' is not defined. Did you mean: 'complex'?
complex(True)
(1+0j)
complex(False)
0j
complex(5+8j)
(5+8j)
#Boolean
bool(7)
True
bool(9.8)
True
bool("Hi")
True
bool(6+9j)
True
bool(True)
True
bool(False)
False
