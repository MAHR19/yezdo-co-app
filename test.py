import psycopg2
import subprocess

connection = psycopg2.connect(
    dbname='Catalagos_DB',
    user='yezdo',
    password='Mahr1119;.',
    host='0.0.0.0',
    port='5432'
)

print (connection.closed) # 0

# restart the db externally
#subprocess.check_call("sudo /etc/init.d/postgresql restart", shell=True)
#
## this query will fail because the db is no longer connected
#try:
#    cur = connection.cursor()
#    cur.execute('SELECT 1')
#except psycopg2.OperationalError:
#    pass
#
#print connection.closed # 2
