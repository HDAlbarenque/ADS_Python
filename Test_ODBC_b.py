from icecream import ic
import pyodbc

str_sql = (
    "Driver={Advantage StreamlineSQL ODBC};"
    "SERVER=local;"
    r"DataDirectory=C:\UNIRE\PS-DATOS\UNIRE.add;"
    "DATABASE=UNIRE;"
    "UID=AdsSys;"
    "PWD=/-789;"
    "ServerTypes=1;"
    )

print(str_sql)

connection = pyodbc.connect(str_sql,autocommit=True)

if connection:
    print("Yes, we are connected!\n")

sql = '''\
SELECT CLAVE, NOMBRE
FROM PROCESOS
'''

cursor = connection.execute(sql)
for c in cursor:
    print(c[0], c[1])
