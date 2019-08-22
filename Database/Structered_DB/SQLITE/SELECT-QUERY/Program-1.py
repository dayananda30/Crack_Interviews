import sqlite3


class TableData:
    def __init__(self,database):
        print("I am inside Constructor")
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()

    def createTable(self):
        try :
            self.c.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(
                        StudentName text,
                        RollNum int PRIMARY KEY,
                        Place text,
                        FavSubject text,
                        Mark int,
                        Result text
                        )''')
        except sqlite3.OperationalError as e:
            #print("Couldn't create the Table Due to : {}".format(e))
            pass

    def addValues(self,sname,rnum,place,favsub,marks,res):
        try:
            self.c.execute('INSERT INTO STUDENTS VALUES ("{}", {}, "{}", "{}", {}, "{}")'.format(sname,rnum,place,favsub,marks,res))
        except sqlite3.IntegrityError as e:
            pass
        self.conn.commit()
        print("Added successfully")

    def display(self):
        print(self.c.execute("""SELECT * FROM STUDENTS""").fetchall())
        print(self.c.execute("""SELECT StudentName FROM STUDENTS""").fetchall())
        print(self.c.execute("""SELECT StudentName FROM STUDENTS WHERE RollNum=4""").fetchall())
        print(self.c.execute("""SELECT StudentName FROM STUDENTS ORDER BY Mark""").fetchall())
        print(self.c.execute("""SELECT * FROM STUDENTS LIMIT 3 OFFSET 3""").fetchall())
        print(self.c.execute("""SELECT DISTINCT Place FROM STUDENTS""").fetchall())


    def __del__(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    student = TableData('demo.db')
    student.createTable()
    student.addValues('ARUN',1,'BENGALURU','MATH',500, 'PASS')
    student.addValues('BHARATH',2,'BENGALURU','MATH',520, 'PASS')
    student.addValues('CHANDAN',3,'BENGALURU','SCIENCE',503, 'PASS')
    student.addValues('DAYA',4,'KOLAR','SCIENCE',489, 'PASS')
    student.addValues('ERIC',5,'GOA','SOCIAL',400, 'PASS')
    student.addValues('FERNANDIES',6,'GOA','ENGLISH',550, 'PASS')
    student.addValues('GURU',7,'KOLAR','MATH',505, 'PASS')
    student.addValues('HEMANTH',8,'BENGALURU','MATH',545, 'PASS')
    student.addValues('ISHANTH',9,'BENGALURU','MATH',556, 'PASS')
    student.addValues('JAYANTH',10,'BENGALURU','MATH',467, 'PASS')
    student.display()

