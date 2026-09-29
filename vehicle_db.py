import mysql.connector


class VehicleListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='Agna',
            host='localhost',
            database='vehicle_db'
        )

        print(self.connection)

        self.cursor = self.connection.cursor()

        print("successfully connected")

    def list(self):
        # reading all records from db table
        query = "SELECT * FROM vehicle"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:
            for row in records:
                print(row)
        else:
            print("no records found")

    def create(self,brand, model, type, price, year):
        # creating a new record
        query = """
        INSERT INTO vehicle(brand, model, type, price, year)
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (brand, model, type, price, year)

        self.cursor.execute(query, data)

        self.connection.commit()

        print("inserted data successfully")

    def retrieve(self, id):
        query = "SELECT * FROM vehicle WHERE id = %s"

        data = (id,)

        self.cursor.execute(query, data)

        records = self.cursor.fetchone()

        if records:
            print(records)
        else:
            print("no records found")

    def delete(self, id):
        query = "DELETE FROM vehicle WHERE id = %s"

        data = (id,)

        self.cursor.execute(query, data)

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("deleted successfully")
        else:
            print("no records found")

    def update(self, id, brand, model, type, price, year):
        query = """
        UPDATE vehicle
        SET brand = %s,
            model = %s,
            type = %s,
            price = %s,
            year = %s
        WHERE id = %s
        """

        data = (brand, model, type, price, year, id)

        self.cursor.execute(query, data)

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("updated successfully")
        else:
            print("no records found")

b = VehicleListCreateRetrieveUpdateDelete()

b.list()

b.create("Toyota", "Innova", "SUV", 2500000, 2024)

b.list()
b.retrieve(1)
b.update(2, "Honda", "City", "Sedan", 1500000, 2023)
b.delete(5)













