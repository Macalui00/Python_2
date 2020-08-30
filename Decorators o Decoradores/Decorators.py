"""DECORATORS:
Son funciones
Envuelven otras funciones y mejoran su comportamiento
Son ejemplos de funciones de orden superior
Tienen su propia sintaxis, usando "@" (Azucar sintactico)
"""

#Decorators como funciones:
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite #Esto me evita...
def greet():
    print("My name is Colt.")
    
@be_polite #Esto me evita...
def rage():
    print("I HATE YOU!")

#Me evita esto:
# polite_rage = be_polite(rage)
# greet = be_polite(greet)
# greet()
# polite_rage()

greet()
rage()