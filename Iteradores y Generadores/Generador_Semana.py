#Definir una funcion generadora weel que tiene una lista de dias.
#Iterar todos los dias. Una vez llegado el domingo, no debe comenzar de nuevo

def semana():
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    for dia in dias:
        yield dia