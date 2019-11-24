import cx_Oracle
import pandas as pd

class Connection(cx_Oracle.Connection):

  def cursor(self):
    cursor = super(Connection, self).cursor()
    cursor.arraysize = 10000
    return cursor

conn = Connection("dba_ho", "yvc02tvf", "mbsho")

# prints 5000
print(conn.cursor().arraysize)

archivos_clientes = "prueba_archivo.csv"
listado_cli = open(archivos_clientes,'w')

df = pd.read_sql_query("select store_no,cust_no,cust_check_dig,status from cust where store_no = 1 and rownum < 10 order by store_no,cust_no", conn)

df.to_csv(archivos_clientes,sep=';')

print(df)

df1 = pd.DataFrame(df, columns= ['store_no','cust_no','cust_check_dig','status'])

print(df1)

export = df1.to_json(r'archivo_json.json')

print(export)