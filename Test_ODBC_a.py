from icecream import ic
import pyodbc

sql_a = r"Driver={Advantage StreamlineSQL ODBC};"
sql_b = r"SERVER=local;"
sql_c = r"DataDirectory=C:\UNIRE\PS-DATOS\UNIRE.add;"
sql_d = r"DATABASE=UNIRE;"
sql_e = r"UID=AdsSys;"
sql_f = r"PWD=/-789;"
sql_g = r"ServerTypes=1;"
str_sql = sql_a + sql_b + sql_c + sql_d + sql_e + sql_f + sql_g 


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
