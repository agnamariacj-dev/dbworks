import mysql.connector
con=mysql.connector.connect(user="root",password="Agna",host="localhost",database="school_db")
print(con)
c=con.cursor()
query="delete from student where roll_no=%s"
data=(101,)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("Data is deleted")
else:
    print("No record found")
