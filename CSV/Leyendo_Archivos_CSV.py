import csv

#Manera sencilla de leer un csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file) #retorna un objeto iterable reader
    #Este objeto se itera con un for que imprime el contenido de cada linea:
    for row in reader:
        print(row)

"""Su output:
    ['SN', 'Name', 'Contribution']
    ['1', 'Linus Torvalds', 'Linux Kernel']
    ['2', 'Tim Berners-Lee', 'World Wide Web']
    ['3', 'Guido van Rossum', 'Python Programming']
"""
#Ahora veamos como customizar el reader:
#La coma es utilizada como delimitador de default de un archivo CSV. Aun así, algunos archivos utilizan delimitadores diferentes, como pueden ser el pipe (|) o el tab (\t)

#Imaginemos que el archivo esta utilizando como delimitador el tab. Para leer el archivo podemos pasar un parametro adicional "delimiter" al csv.reader()
# with open('innovators.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = '\t')
#     for row in reader:
#         print(row)

#Y como output me retornará lo mismo

#Ahora bien, hay algunos archivos CSV que contienen espacios antes del delimitador. Cuando usamos la funcion de default csv.reader() para leer archivos csv, obtendremos espacios en el output claramente.
#Para poder remover estos espacios iniciales, necesitamos pasarle un parametro adicional llamado: skipinitialspace:
#Tenemos el archivo people.csv como ejemplo

with open('people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

#si esto lo ejecutamos, veremos que nos omitio los espacios.

#Puede pasar que tenga archivos CSV con comillas en todas o algunas de sus entradas. Usemos de ejemplo el archivo quotes.csv
#Con el parametro opcional quoting podemos omitir o quitar estas comillas

with open('person1.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)

#Al poner quote_all estoy indicando que todos los valores en el archivo presentan comillas.
#Hay tres constantes predefinidas que se le pueden pasar al paremtro quoting:
#csv.QUOTE_MINIMAL: Especifica al reader que el archivo solo presenta comillas en aquellas entradas que contienen caracteres especiales como delimitador.
#csv.QUOTE_NONNUMERIC: Especifica al reader que el archivo contiene comillas en las entradas no numericas.
#csv.QUOTE_NONE: no hay ninguna comilla en ninguna entrada.

#Ahora bien, todos estos parametros que utilizamos queda bien utilizarlo asi cuando lideamos con uno o dos archivos csv pero cuando vamos a lidear con muchos archivos que tienen una estructura similar,
#hay una mejor manera de realizar esto: dialect que es un parametro opcional, el cual me permite agrupar varios patrones de formato como lo son delimiter, skipinitialspace, quoting, escapechar en un solo nombre dialect
#y esto puede ser pasado como parametro en multiples writers y readers.

#Utilizando el archivo: office.csv
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('office.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

"""Esta info tan interesante fue obtenida de: https://www.programiz.com/python-programming/reading-csv-files"""
#------------------------------------------------------------------------------------------------------------
#Abrimos el archivo indicado como csv_file
with open('employee_birthday.txt') as csv_file:
    #Leo ese archivo indicandole como delimitador la ,
    csv_reader = csv.reader(csv_file, delimiter=',')
    #Utilizo una variable para saber cual es la linea de nombre de las columnas y cuales son las lineas de información
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    #Indico cuantas lineas fueron procesadas:
    print(f'Processed {line_count} lines.')

"""Información que me retorna:
Column names are name, department, birthday month
    John Smith works in the Accounting department, and was born in November.
    Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.
"""


"""Esta data tan interesante ha sido obtenida de: https://realpython.com/python-csv/"""