import mysql.connector
con=mysql.connector.connect(user="root",password="Agna",host="localhost",database="school_db")
print(con)
c=con.cursor()
query="Select * from student where roll_no=%s"  #Read a specific record from db table
data=(101,) #data=(102,) #no record found
c.execute(query,data)
record=c.fetchone()
if record:
    print(record)
else:
    print("No record found")
c.close()
con.close()