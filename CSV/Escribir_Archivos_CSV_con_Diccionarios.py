#Escribir archivos CSV con diccionarios:

import csv

#Abro el archivo en modo de escritura
with open('employee_file2.csv', mode='w') as csv_file:
    #Nombres de las columnas:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    #Escribo la cabecera
    writer.writeheader()
    #Escribo las lineas:
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})