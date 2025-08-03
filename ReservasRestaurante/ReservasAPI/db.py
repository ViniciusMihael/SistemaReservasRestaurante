from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///restaurante.sqlite3", echo=True)

conn = engine.connect()

print(conn.connection.dbapi_connection)

conn.close()