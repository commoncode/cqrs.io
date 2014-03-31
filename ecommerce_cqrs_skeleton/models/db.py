import sqlite3
import os.path
def _execute(query):
    dbPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/ecommerce.db"))
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
            cursorobj.execute(query)
            # result = cursorobj.fetchall()
            connection.commit()
    except Exception:
            raise
    #connection.close()
    return cursorobj
