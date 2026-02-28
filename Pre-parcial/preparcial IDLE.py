Python 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = input("Digite un texto: ")
Digite un texto: Jefferson
>>> print(msg[0])
J
>>> print(msg[-1])
n
>>> if (len(msg)>5):
...     print("Palabra larga")
... else:
...     print("Palabra corta")
... 
Palabra larga
>>> Print(len(msg))
Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "<pyshell#9>", line 1, in <module>
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print(len(msg))
9
