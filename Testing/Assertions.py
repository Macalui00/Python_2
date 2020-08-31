""" ASSERTIONS / ASERCIONES:
Podemos hacer simples aserciones con la palabra clave assert
Assert acepta una expresion
Retorna None si la expresion es verdadera
Tira un AssertionError si la expresion es falsa
Acepta un mensaje opcional de error como segundo argumento
"""
#Ejemplo:
def sumar_numeros_positivos(x,y):
    assert x > 0 and y > 0, "Ambos números deben ser positivos!"
    return x + y

print(sumar_numeros_positivos(1,1)) # 2
# sumar_numeros_positivos(1,-1) # AssertionError: Ambos números deben ser positivos!

#Otro ejemplos:
# print(assert 4==4)
# print(assert 4 == 2) # AssertionError
# print(assert 4 == 2, "4 no es igual a 2!!!") # AssertionError: 4 no es igual a 2!!!

#Otro más
def eat_junk(food):
    assert food in ["pizza", "helado", "caramelos", "hamburguesa", "papas fritas", "pancho"], "La comida debe ser comida chatarra."
    return f"ÑUM ÑUM ÑUM estoy comiendo un(a/o)(s) {food}"

food = input("Ingrese una comida chatarra: ")
print(eat_junk(food))

#Assertions Warning: Si un archivo python es ejecutado con el -O flag, las aserciones no seran evaluadas!
#Esto pasa si por consola pongo lo siguiente:
# python -O assertions.py
#Lo que hará es que si ejecuto el programa, e inserto algo incorrecto como por ejemplo: zanahorias, no saltará el error.

#No escribas codigo como este!!
"""
def do_something_bad(user):
    assert user.is_admin, "Only admins can do bad things"
    destroy_a_brunch_of_stuff()
    return "Mua ha ha ha!"
"""

