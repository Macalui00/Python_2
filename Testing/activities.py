from random import choice

def eat(food, is_healthy):
    #Vamos a agregar un chequeo de si is_healthy no es una instancia de boolean despues tiramos un error de valor
    if isinstance(is_healthy, bool): #Si no colocabamos esto, el testeo de si es o no un booleano en test.py nos da un error
        raise ValueError("is_healthy debe ser un booleano!")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours >2:
        return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours!"
    else:
        return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return choice("lol", "haha", "tehehe")