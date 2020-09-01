"""Unit testing
Test smallest parts of an aplication in isolation (en aislamiento)(e.g. units)
Good candidates for unit testing: individual classes, modules or functions
Bad candidates for unit testing: an entire aplication, dependencies across several clases or modules

Acá mucha documentación de cosas que podes probar:
https://docs.python.org/3/library/unittest.html

Python viene con un modulo construido llamado unittest
Podes escribir pruebas unitarias encapsuladas como clases que heredan desde unittest.TestCase

supongamos que tenemos dos archivos:
activities.py

def eat(food, is_healthy):
    pass

def nap(num_hours):
    pass

test.py

import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    pass

if ___name___ = '__main__':
    unittest.main()

"""