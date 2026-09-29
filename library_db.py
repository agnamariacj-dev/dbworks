import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="Agna",host="localhost",database="library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("Successfully connected")


    def list(self):
        #read all records from db table
            query="select * from book"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("No records")

    def create(self,title,author,price,pages,language):
            query="insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)";
            data=(title,author,price,pages,language)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("Inserted data successfully")
    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No record found")

    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("deleted data successfully")
        else:
            print("No record found")



    def update(self,id,title,author,price,pages,language):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("Updated data successfully")
        else:
            print("No record found")

b=BookListCreateRetrieveUpdateDelete()
b.list()
b.create('ABC',"john",300,500,"English")
b.retrieve(4)
b.delete(4)
b.update(3,"STU","moke",300,400,"english")