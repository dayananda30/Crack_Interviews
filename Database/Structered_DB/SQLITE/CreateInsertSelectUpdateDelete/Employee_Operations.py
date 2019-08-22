import sqlite3

class EmployeeOperations:
    def __init__(self):
        self.conn = sqlite3.connect('employees.db')
        #self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS employees(
                name text,
                empId int PRIMARY KEY,
                dept text,
                manager text,
                salary int
                )""")

        except sqlite3.OperationalError as e:
            pass
            #print("Couldn't create Employee table due to '{}'".format(e))


    def addNewEmployee(self,name, empId, dept, manager, salary):
        self.name = name
        self.empId = empId
        self.dept = dept
        self.manager = manager
        self.salary = salary
        try:
            self.c.execute("INSERT INTO employees VALUES ('{}', {}, '{}', '{}', {} )".format(self.name, self.empId, self.dept, self.manager, self.salary))
        except sqlite3.IntegrityError as e:
            print("Failed to Insert the element due to - {}".format(e))
        self.conn.commit()

    def updateSalaryDetails(self,empId,salary):
        try:
            self.c.execute("UPDATE employees SET salary={},manager='Piyush' WHERE empId={}".format(salary,empId))
            self.conn.commit()
        except Exception as e:
            raise e.message

    def deleteEmployee(self, empId):
        try:
            self.c.execute("DELETE FROM employees WHERE empid=332943")

        except Exception as e:
            raise e.message

    def display(self):
        #print("{}".format(self.c.execute("""SELECT * FROM employees""")))
        print(self.c.execute("""SELECT * FROM employees""").fetchall())
        #print(self.c.fetchall())

    def __del__(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    emp = EmployeeOperations()
    emp.addNewEmployee('Dayananada', 20006381, 'RealProtect', 'Sham', '3000')
    emp.addNewEmployee('Dayananda D R', 332943, 'NHC', 'Usha', '2000')
    emp.display()
    emp.updateSalaryDetails(20006381,565656)
    emp.display()
    emp.deleteEmployee(332943)
    emp.display()
