import DbOperations

backend_stuff = DbOperations.DatabaseOperation()
backend_stuff.db_connect()

print(backend_stuff.conn)
