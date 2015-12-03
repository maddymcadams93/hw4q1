from sqlalchemy import create_engine

engine = create_engine('postgresql://hw4:w4111@w4111db1.cloudapp.net/iowa')
conn = engine.connect()
conn.execute('select 1')

def buggy_sanitize_1(input):
    return input.replace(';', '\;')

input = "1 = 1\; SELECT 1 WHERE 1 = 1"
query = "SELECT 1 WHERE 1 = 0 and %s;" % buggy_sanitize_1(input)
cursor = conn.execute(query)
print (cursor.rowcount)
