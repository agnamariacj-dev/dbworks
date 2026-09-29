import mysql.connector
con=mysql.connector.connect(user="root",password="Agna",host="localhost",database="school_db")
print(con)
c=con.cursor()
query="Select * from student"
c.execute(query)
records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("No records found")
c.close()
con.close()