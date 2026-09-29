import mysql.connector

#establish connection between mysql server and python code
# con=mysql.connector.connect(user="root",password="Agna",host="localhost")

#it returns connection object
# print(con)
#
# #cursor object --for executing sql queries
# c=con.cursor()
#
# # query="create database school_db"
# # c.execute(query)
#
# print("Database file created")
# c.close()
# con.close()



#creating table
con=mysql.connector.connect(user="root",password="Agna",host="localhost",database="school_db")
print(con)
c=con.cursor()
# query="""create table student(
#                                 roll_no int not null primary key,
#                                 name varchar(20),
#                                 age int,
#                                 place varchar(20),
#                                 phone varchar(20),
#                                 total_mark int)""";
# c.execute(query)
# print("Table Created")

#create new record/insert data into database table student
query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"

data=(101,"arun",11,"ekm","7567675679",145)

c.execute(query,data)
con.commit()
print("Inserted data successfully")
c.close()
con.close()

































