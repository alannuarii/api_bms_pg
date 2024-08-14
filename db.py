import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection(query, action, value=None):
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'), 
            password=os.getenv('DB_PASSWORD'),
            dbname=os.getenv('DB_NAME')
        )

        cur = conn.cursor()
        if action == 'select':
            cur.execute(query, value)
            result = cur.fetchall()
            return result
        elif action in ['insert', 'update', 'delete']:
            cur.execute(query, value)
            conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
