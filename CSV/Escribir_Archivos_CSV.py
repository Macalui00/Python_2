#Escribir archivos CSV:

import csv

with open('employee_file.csv', mode='w') as employee_file:
    #Indico el delimitador el quotecharacter y demás
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #Inserto las lineas al archivo:
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])