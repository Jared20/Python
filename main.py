"""
#módulo principal
import operaciones#importamos el módulo

print(operaciones.a)

operaciones.funcion1('hola mundo')

print(operaciones.funcion2())

import operaciones as op

print(op.funcion2())

from operaciones import funcion2,funcion1,a

print(funcion2())
funcion1('hola')
print(a)
"""
#import carpeta.interfaz as ci

#print(carpeta.interfaz.a)
#print(ci.b)
from carpetin import interfaz as i
print(i.a)
print(i.b)
print(i.c)