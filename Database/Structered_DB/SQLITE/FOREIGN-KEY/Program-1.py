import sqlite3
import pandas
import os
class Example:
    def __init__(self,database):
        if os.path.exists(database):
            os.remove(database)
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()

    def createTable(self):
        try :
            self.c.execute('''PRAGMA foreign_keys=ON''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS COLOURS(
                        NAME text UNIQUE
                        )''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS CARS(
                        MODEL text,
                        YEAR int,
                        COLOUR text REFERENCES COLOURS(NAME) ON UPDATE CASCADE ON DELETE CASCADE
                        )''')

        except sqlite3.OperationalError as e:
            #print("Couldn't create the Table Due to : {}".format(e))
            pass

    def addColours(self, new_color):
        try:
            self.c.execute('INSERT INTO COLOURS VALUES ("{}")'.format(new_color))
            self.conn.commit()
        except Exception as e:
            print(e.message)

    def addCars(self, model, year, colour):
        try:
            self.c.execute('INSERT INTO CARS VALUES ("{}", {}, "{}")'.format(model,year,colour))
            self.conn.commit()
        except Exception as e:
            print(e.message)

    def deleteColour(self, colour):
        self.c.execute('DELETE FROM COLOURS WHERE NAME = "{}" '.format(colour))
        self.conn.commit()
        print("'{}' colour deleted successfully".format(colour))

    def updateColour(self, old_colour, new_colour):
        self.c.execute('UPDATE COLOURS SET NAME = "{}" WHERE NAME = "{}"'.format(new_colour, old_colour))
        self.conn.commit()
        print("Updated successfully")

    def displayTableData(self, table):
        print("Printing '{}' TABLE VALUES ".format(table))
        print("*"*30)
        print(pandas.read_sql_query('''SELECT * FROM "{}"'''.format(table), self.conn))

if __name__ == '__main__':
    obj = Example('Example.db')
    obj.createTable()
    print("Adding Colours")
    obj.addColours("YELLOW")
    obj.addColours("GREEN")
    obj.addColours("BLACK")
    obj.addColours("BLUE")
    obj.addColours("WHITE")
    print("Colours added sucessfully")

    print("Adding cars")
    obj.addCars('Maruti 800', 2000, 'GREEN')
    obj.addCars('BMW', 2000, 'WHITE')
    obj.addCars('AUDI', 2000, 'BLACK')
    obj.addCars('Ford Fiesta', 2000, 'YELLOW')
    obj.addCars('Volks Wagon', 2000, 'GREEN')
    print("Cars are added successfully")

    obj.displayTableData('COLOURS')
    obj.displayTableData('CARS')

    print("USECASE 1 : Trying to add a CAR of Colour ORANGE which is not there in COLOUR table")
    obj.addCars('Volks Wagon new', 2000, 'ORANGE')
    print("It is Failed because you're trying to insert a car with Colour ORANGE which is not there in COLOURS table")


    print("USECASE 2 : Inserting ORANGE to COLOUR table and trying to add same car with ORANGE colour")
    obj.addColours('ORANGE')
    obj.addCars('Volks Wagon new', 2000, 'ORANGE')
    obj.displayTableData('CARS')


    print("USECASE 3 : Whenever COLOUR table is updated , its referenced row tabled in the referrring TABLE must be updated.")
    print("For eg : If I remove 'GREEN' colour from COLOUR table, Maruti 800 and Volks Wagon car records from CAR table must be removed")
    obj.deleteColour('GREEN')
    obj.displayTableData('CARS')


    print("USECASE 4 : Whenver I update COLOUR table, the COLUMN from CAR which is referring COLOUR table should be updated")
    print("For ex : If I update BLACK COLOUR with PURPLE in COLOUR table , AUDI car in CAR table should be updated.")
    obj.updateColour('BLACK', 'PURPLE')
    obj.displayTableData('COLOURS')
    obj.displayTableData('CARS')







