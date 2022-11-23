import pandas as pd
# string "Hello World"

for i in range(1000):
	print("Hello World")

accept
# world string
# run plsql using Python.

import cx_Oracle
import pandas as pd

# connect to Oracle
conn = cx_Oracle.connect('user/password@host:port/sid')

# create a cursor
cur = conn.cursor()

# execute a statement
cur.execute('select * from table')

