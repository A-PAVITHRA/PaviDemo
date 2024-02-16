
from database import create_connection

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def my_custom_sql(sqlquery, substitute):  # only for insert query
    connection = create_connection()
    with connection.cursor() as cursor:
        row = cursor.execute(sqlquery, substitute)
        connection.commit()
    return row

def my_custom_get_sql(sqlquery, substitute):  #for view purpose only
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute(sqlquery, substitute)
        row = dictfetchall(cursor)
    return row
