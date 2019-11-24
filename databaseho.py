import cx_Oracle
from sqlalchemy import create_engine
#from decouple import config
from pprint import pprint
import datetime



class OracleDBHo:
    """
       OracleDB Database
    """
    def __init__(self):
        self.username = 'dba_ho'
        self.password = 'yvc02tvf'
        self.hostname = '10.49.2.24'
        self.port = '1525'
        self.sid = 'MBSHO'
        self.engine = None
        self.conn = None
        self.rconn = None
        self.oracle_connection_string = ('oracle+cx_oracle://{username}:{password}@' +
            cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
        )

    def connect(self):
        try:
            self.engine = create_engine(
                self.oracle_connection_string.format(
                    username=self.username,
                    password=self.password,
                    hostname=self.hostname,
                    port=self.port,
                    service_name=self.sid,
                ), pool_size=100)
            self.conn = self.engine.connect()
            self.rconn = self.engine.raw_connection()
            return self.conn
            print("conected...")

        except cx_Oracle.DatabaseError as e:
            self.engine = None
            print(e)
            exit(1)

    def connection_close(self):
        self.conn.close()
        print("Not Conected...")


if __name__ == '__main__':
    ora = OracleDBHo()
    ora.connect()
    ora.connection_close()