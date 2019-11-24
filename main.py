from databaseho import OracleDBHo
from databasest01 import OracleDBSt01
import pandas as pd
import io
from flask import jsonify


archivos_clientes = "clientes_st01"

def cliente_st01():
    l_cust01 = clist01()
    #
    print (len(l_cust01))
    return l_cust01

def clist01():
    sqlString = """select store_no ,cust_no,cust_check_dig,cust_status from cust
                    order by store_no,cust_no"""
    ora = OracleDBSt01().connect()
    res = ora.execute(sqlString)
    data_cust01 = res.fetchall()
    return data_cust01

def cliente_ho():
    l_custho = clistho()
    #array_test = []
    content = {}
    for r in l_custho:
        content = {r}
        #array_test.append(content)
    #return array_test
        print(content)
    return content

def clistho():
    sqlString = """select 'tineda '||store_no ,' cliente '||cust_no,' digito_verifcador '||cust_check_dig,' estado '||status
                    from cust
                    where store_no = 1
                    and rownum = 1
                    order by store_no,cust_no"""
    ora = OracleDBHo().connect()
    res = ora.execute(sqlString)
    for result in res:
        print (result)
    return result

def cliho():
    sqlstr = """select *
                    from cust
                    where store_no = 1
                    and rownum = 1
                    order by store_no,cust_no"""
    ora = OracleDBHo().connect()
    return sqlstr


archivos_clientes = "prueba_archivo.csv"
listado_cli = open(archivos_clientes,'w')
#titulos = "tienda_ho","cliente_ho","digito_verificador_ho","estado_ho","tienda_st01","cliente_st01","digito_verificador_st01","estado_st01\n"
titulos = "tienda_ho","cliente_ho","digito_verificador_ho","estado_ho"

cliente_ho()
ora = OracleDBHo().connect()
df = pd.read_sql_query(cliho,ora)
df.to_csv(archivos_clientes,sep=';')

print(df)