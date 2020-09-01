import pandas

df = pandas.read_csv('hrdata.csv')
print(df)

"""Algunas cosas para notar:
Primero, pandas reconocer que la primera linea del CSV contiene los nombres de las columnas y los usa automaticamente.
De cualquier manera, pandas esta usando indices enteros base cero.
Tipos de datos de las columnas: las columnas de numeros las corrige correctamente pero en el caso de fecha lo convierte a un string"""

print(type(df['Hire Date'][0]))
# <class 'str'>

#Abordando un problema por vez...
#Seleccionemos un indice de columna para tener una columna diferente como indice:
df = pandas.read_csv('hrdata.csv', index_col='Name')
print(df)

#Para corregir la fecha hay qeu forzar con pasa la lectura de estos datos como fecha:
df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)

print(type(df['Hire Date'][0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

#Si sus archivos CSV no tienen nombres de columna en la primera línea, puede usar el parámetro opcional names para proporcionar una lista de nombres de columna.
#También puede usar esto si desea anular los nombres de columna proporcionados en la primera línea. En este caso, también debe indicarle a pandas.read_csv() que ignore los nombres de las columnas existentes mediante el parámetro opcional header=0:
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)


"""Esta data tan interesante fue obtenida de: https://realpython.com/python-csv/"""