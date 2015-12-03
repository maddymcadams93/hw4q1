from sqlalchemy import create_engine

engine = create_engine('postgresql://hw4:w4111@w4111db1.cloudapp.net/iowa')
conn = engine.connect()
conn.execute('select 1')

def buggy_sanitize_2(input):
    return input.replace(';', '\;').replace("\'", "\\'")

input = "1’ UNION SELECT 2--"
query = "SELECT 1 WHERE 'foo' = '%s';" % buggy_sanitize_2(input)
cursor = conn.execute(query)
print (cursor.fetchall()[0][0])
