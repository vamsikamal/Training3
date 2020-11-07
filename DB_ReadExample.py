import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=DESKTOP-JPG196B\\SQLEXPRESS;Database=dbSLC;Trusted_Connection=yes;')
cursor = conn.cursor()
sql_command = "SELECT * FROM tblStudent"  #
cursor.execute(sql_command)
for row in cursor:
    #print(row)
    print(row.FirstName)
    #print(row[1])
conn.close()