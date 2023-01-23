import sqlite3
import subprocess
dbname = 'main.db'
conn = sqlite3.connect(dbname)


cur = conn.cursor()


cur.execute(
    "CREATE TABLE IF NOT EXISTS hwidauth (hwid text)"
)
def GetUUID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    cur.execute("INSERT INTO hwidauth VALUES (?)", [uuid])
    conn.commit()

GetUUID()
cur.execute('SELECT * FROM hwidauth')
for row in cur:
    print(row)
conn.close()
