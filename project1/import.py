import psycopg2

conn = psycopg2.connect(
    "host='localhost' post='5432' dbname='' user='' password=''")
cur = conn.cursor()

cur.copy_from(r'../project1/books.csv', temp_unicommerce_status)

conn.close()
