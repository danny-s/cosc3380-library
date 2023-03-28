import psycopg2
import psycopg2.extras
import random
from faker import Faker
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host= '127.0.0.1',
        database= 'cosc',
        user="kevin",
        port = 5432
    )
    cur = conn.cursor()
    view_script = ''' '''   #Write you sql code in here
    cur.execute(view_script) #This will execute your sql code in here



    conn.commit() #Will push the sql code from Python to your SQL database
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()










