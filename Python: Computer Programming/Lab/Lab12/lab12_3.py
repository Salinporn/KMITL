class Name:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return f"{self.title}. {self.firstName} {self.lastName}"


class Date:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"

    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year+543}"


class Address:
    def __init__(self, houseNO, street, district, city, country, postcode):
        self.houseNO = houseNO
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def setAddress(self, houseNO, street, district, city, country, postcode):
        self.houseNO = houseNO
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return f"{self.houseNO} {self.street} {self.district} {self.city} {self.country} {self.postcode}"


class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList

    def addEmployee(self, e):
        self.employeeList += [e]
        e.department = self

    def deleteEmployee(self, e):
        self.employeeList.remove(e)
        e.department = None

    def setManager(self, e):
        if type(e) == PermEmployee and e in self.employeeList:
            self.manager = e

    def printinfo(self):
        print(f"Description: {self.description}"
              f"\nManager: {self.manager.firtname} {self.manager.lastname}"
              f"\nemployeeList: {self.employeeList}")


class Person:
    def __init__(self, name, date, address):
        self.name = name
        self.birthdate = date
        self.address = address

    def printInfo(self):
        print(f"Name: {self.name.getFullName()}"
              f"\nBirthdate: {self.birthdate.getDate()}"
              f"\nAddress: {self.address.getAddress()}")


class Employee(Person):
    def __init__(self, name, date, address, startDate, startMonth, startYear, department):
        super().__init__(name, date, address)
        self.startDate = startDate
        self.startMonth = startMonth
        self.startYear = startYear
        self.department = department

    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()}" 
              f"\nAddress: {self.address.getAddress()}"
              f"\nStart date: {self.startDate}/{self.startMonth}/{self.startYear}"
              f"\nDepartment: {self.department}")


class TempEmployee(Employee):
    def __init__(self, name, date, address, startDate, startMonth, startYear, department, wage):
        super().__init__(name, date, address, startDate, startMonth, startYear, department)
        self.wage = wage

    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()}"
              f"\nAddress: {self.address.getAddress()}"
              f"\nStart date: {self.startDate}/{self.startMonth}/{self.startYear}"
              f"\nDepartment: {self.department} Wage: {self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, date, address, startDate, startMonth, startYear, department, salary):
        super().__init__(name, date, address, startDate, startMonth, startYear, department)
        self.salary = salary

    def printInfo(self):
        print(f"Name: {self.name.getFullName()} Birthday: {self.birthdate.getDate()} "
              f"\nAddress: {self.address.getAddress()} "
              f"\nStart date: {self.startDate}/{self.startMonth}/{self.startYear} "
              f"\nDepartment: {self.department} Salary: {self.salary} ")