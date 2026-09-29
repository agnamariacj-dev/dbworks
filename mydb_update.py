import mysql.connector
con=mysql.connector.connect(user="root",password="Agna",host="localhost",database="school_db")
print(con)
c=con.cursor()
#update
query="update student set name=%s where roll_no=%s"
data=('amal',101)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("record updated")
else:
    print("no record found")

