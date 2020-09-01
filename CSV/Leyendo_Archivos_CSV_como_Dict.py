#Leyendo archivos CSV como diccionarios:
import csv

#Manera sencilla de leer archivos csv con diccionarios:
with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

"""OUTPUT:
{'Name': 'Jack', ' Age': ' 23', ' Profession': ' Doctor'}
{'Name': 'Miller', ' Age': ' 22', ' Profession': ' Engineer'}
"""
#La sintaxis completa de DictReader(): csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

"""Esta info tan interesante fue obtenida de: https://www.programiz.com/python-programming/reading-csv-files"""

#---------------------------------------------------------------------------------------------------------------
#Indico modo de lectura (r)
with open('employee_birthday.txt', mode='r') as csv_file:
    #Indico que leo el archivo csv como diccionario:
    csv_reader = csv.DictReader(csv_file)
    #Variable para contar la cantidad de lineas y diferenciar lo que serían los titulos de las columnas de lo que es la info
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

"""Lo que me retorna:
Column names are name, department, birthday month
    John Smith works in the Accounting department, and was born in November.
    Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.

De donde vienen las keys del diccionario? de la primera linea del CSV, que asume que contiene las llaves
para construir el diccionario. Si no tenes en tu CSV estas llaves, podes setearlas con el parametro opcional fieldname
"""

"""Esta data tan interesante ha sido obtenida de: https://realpython.com/python-csv/"""