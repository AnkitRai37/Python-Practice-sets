class Student:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
student1 = Student('Ankit', 20, 25000)
print(student1.name, student1.age, student1.salary)
student2 = Student('Dheeraj', 25, 35000)
print(student2.name, student2.age, student2.salary)


class Book:
    def __init__(self, tittle, author, price):
        self.tittle = tittle
        self.author = author
        self.price = price
Book1 = Book("Aryabhatta's life", "Ramchandra", 1500)
print(Book1.tittle, Book1.author, Book1.price)
Book2 = Book("Ghar Tak", "dVENDRA sINGH", 2500)
print(Book2.tittle, Book2.author, Book2.price)
Book3 = Book("Krishnadas", "Christopher Nolan", 10000)
print(Book3.tittle, Book3.author, Book3.price)



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
car1 = Car('Mercedes', 'Classic', 2023)
print(car1.brand, car1.model, car1.year)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def has_passed(self):
        return self.marks >= 40
student1 = Student('Ankit Rai', 55)
print(student1.name,"Passed", student1.has_passed())
student2 = Student('Dheeraj Rai', 35)
print(student2.name,"Passed", student2.has_passed())


#####______Modify or update----------------
class Laptop:
    def __init__(self, brand, RAM):
        self.brand = brand
        self.RAM = RAM
laptop1 = Laptop('Lenevo', 512)
print(laptop1.brand, laptop1.RAM)
laptop1.RAM = 1024
print(laptop1.brand, laptop1.RAM)



class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def Deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Desposite : {amount}, new_balance : {self.balance}")
        else:
            print("Invalid deposite amount")
    def Withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"withdrawn : {amount}, new_balance : {self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawn amount")
    def Display_account_detail(self):
        print(f"account_holder : {self.account_holder}, balance : {self.balance}")
    # def __str__(self):   # -- no need to write these--- print(Book1.tittle, Book1.author, Book1.price), only with str and return
       #  return (f"Account Holder: {self.account_holder}, Balance: {self.balance}")
account1 = BankAccount('Ankit Rai', 10000)
account2 = BankAccount('Dheeraj Rai', 20000)
print(account1.Display_account_detail())
print(account2.Display_account_detail())

print(account1.Deposite(5000))
print(account1.Withdraw(13000))
print(account1.Display_account_detail())
  


class Mobile :
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def Display_updated_value(self):
        print(f"These are the mobiles brand : {self.brand}, model : {self.model}, and price : {self.price}")
mobile1 = Mobile('Ferrari', 'F8 Custom', '8000000USD')
print(mobile1.Display_updated_value())
mobile1.price = 9000000
print(mobile1.Display_updated_value())




class Movie :
    def __init__(self, tittle, director, rating):
        self.tittle = tittle
        self.director= director
        self.rating = rating
movie1 = Movie('Aavesham', 'Thomas JD', '4 Star')
print("Befor deletion :", movie1.__dict__)
del movie1.rating
print("After deletion :",movie1.__dict__)


class Devices:   #----Use Var() or __dict__, both gives same result.
    def __init__(self, laptop, mouse, mobile, keyboard, charger):
        self.laptop = laptop
        self.mouse =mouse
        self.mobile = mobile
        self.keyboard =keyboard
        self.charger =charger
device1 = Devices('Lenevo', 'HP', 'Realme', 'Dell', 'Lenevo company')
print(device1.__dict__)
    #----OR
print(device1.laptop, device1.mouse, device1.mobile, device1.keyboard, device1.charger)
        #----OR
print(f"Laptop: {device1.laptop}, Mouse: {device1.mouse}, Mobile: {device1.mobile}, Keyboard: {device1.keyboard}, Charger: {device1.charger}")




class Employee :
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept= dept
        self.salary = salary
emp1 = Employee('Ankit Rai', 'IT', 30000 )
emp2 = Employee('Anoop Singh', 'HR', 40000 )
emp3 = Employee('Suraj Vishwakarma', 'Sales', 50000 )
emp4 = Employee('Dheeraj Kumar', 'Marketing', 25000 )
emp5 = Employee('Surabh Diwedi', 'Analyst', 35000 )
#---------- store all object in list
employees = [emp1, emp2, emp3, emp4, emp5]
#----- use for loop to print the all emp name
for emp in employees:
    print("Employee names:", emp.name)



class Product :
    def __init__(self, name, price):
        self.name = name
        self.price= price
    def return_discount(self):
            print(f"The product name : {self.name} with disounted price : {self.price}")
#----before giving discount-------
product1 = Product('Maggi', 15)
product2 = Product('Pasta', 20)
print(product1.name, product1.price)
print(product2.name, product2.price)
#----- giving discount in price------
product1.price = product1.price - (product1.price * 0.10)
product2.price = product2.price - (product2.price * 0.20)
#-----after giving discount--------
print(product1.return_discount())
print(product2.return_discount())

#-----------OR-----------

#---------- Little bit of getter nethod, cause of __price attribute is private----------
class Product :
    def __init__(self, name, price):
        self.name = name
        self.__price= price
    def return_discount(self):
        print(f"The product name : {self.name} with disounted price : {self.__price}")
#----before giving discount-------
product1 = Product('Maggi', 15)
product2 = Product('Pasta', 20)
print(product1.return_discount())
print(product2.return_discount())



class Rectangle :
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(f"The area of rectangle is : {self.length * self.width}")
    def perimeter(self):
        print(f"The perimater of rectangle is : {2 * (self.length * self.width)} ")
rect1 = Rectangle(5,8)
rect2= Rectangle(8,13)
print(rect1.area())
print(rect2.area())
print(rect1.perimeter())
print(rect2.perimeter())





class Circle :
    def __init__(self, pie, radius):
        self.pie = pie
        self.radius = radius
    def area(self):
        print(f"The area of circle is : {self.pie * (self.radius)**2}")
    def circumference(self):
        print(f"The perimater of rectangle is : {2 * (self.pie * self.radius)} ")
circle1 = Circle(3.14,5)
circle2= Circle(3.14,9)
print(circle1.area())
print(circle2.circumference())
print(circle1.area())
print(circle2.circumference())


class Customer :
    def __init__(self, cust_name, salary, department):
        self.cust_name = cust_name
        self.__salary= salary
        self.__department = department
    def getter(self):
        print(f"The customer {self.cust_name} with salary {self.__salary} working in the {self.__department} department ")
        #---------OR----------
        return self.__salary, self.__department
customer1 = Customer('Ankit Rai', 150000, 'Data')
customer2 = Customer('Ashok Kumar', 20000, 'AI')
print(customer1.getter())
print(customer2.getter())




#####______Modify or update- of a privete attribute using getter and setter method---------------
class Laptop:
    def __init__(self, brand, Ram, price ):
        self.brand = brand
        self.Ram = Ram
        self.__price = price
    def getter(self):
        return self.brand, self.__price
    def setter(self, new_price):
        self.__price = new_price

laptop1 = Laptop('Lenevo', 512, 55000)
print(laptop1.getter())
laptop1.setter(60000)
print(laptop1.getter())


####-----------Simple example of inheritance ------- Not in the question section--------
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):   # overriding parent method
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):   # overriding parent method
        print(f"{self.name} meows.")

# Usage
animal1 = Animal("lion")
dog1 = Dog("Tommy")
cat1 = Cat("Kitty")
animal1.speak()
dog1.speak()   # Tommy barks.
cat1.speak()   # Kitty meows.


#####------Come back to questions ------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_detail(self):
        return self.name, self.salary
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def show_detail(self):
       return self.name, self.salary, self.department
emp1 = Employee("Ankit Rai", 40000)
manager1 = Manager("Ankit Rai", 40000, "IT") 
print(emp1.show_detail())
print(manager1.show_detail())



class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_detail(self):
        return self.brand, self.model

class Bike(Vehicle):
        def __init__(self,brand, model, CC):
            super().__init__(brand, model)
            self.CC = CC
        def BikeFeature(self): # overriding-------------
            return self.brand, self.model, self.CC
class Car(Vehicle):
        def __init__(self, brand, model, cost):
            super().__init__(brand, model)
            self.cost = cost
        def BikeFeature(self):   # -------overriding-------------
            return self.brand, self.model, self.cost
bike1 = Bike("Yamaha", "Y18", 180 )
car1 = Car("Lamborgini", "L32", "80 thousand doller")
bike1.BikeFeature()
car1.BikeFeature()
print(bike1.BikeFeature())
print(car1.BikeFeature())


class Parents:
    def __init__(self, work, responsibility, managethings):
        self.work = work
        self.responsibility = responsibility 
        self.managethings = managethings

    def display(self):   # Parent version
        return f"Parent: Work = {self.work}, Responsibility = {self.responsibility}, Manages = {self.managethings}"

class Child(Parents):
    def __init__(self, work, responsibility, managethings, friends):
        super().__init__(work, responsibility, managethings)
        self.friends = friends

    def display(self):   # Overriding parent's display
        return f"Child: Work = {self.work}, Responsibility = {self.responsibility}, Manages = {self.managethings}, Friends = {self.friends}"

father = Parents("Central AC", "Provide food to family", "Manage every situation")
son = Child("Central AC", "Provide food to family", "Manage every situation", "It's good to have a friend")

print(father.display())   # Parent version
print(son.display())      # Child version



class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age
    def show_detail(self):
        return (f"The person name is : {self.name}  and his age is : {self.age} ")

class Teacher(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject
        def show_detail(self): # overriding-------------
            return (f"The person name is : {self.name} with age : {self.age} and his subject is : {self.subject}")

p1 = Person("Ankit", 20)
t1 = Teacher("Suraj", 30, "Mathmatics")
print(p1.show_detail())
print(t1.show_detail())


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def show_emp_detail(self):
        return (f"emp_id : {self.emp_id}, with name : {self.name} and salary : {self.salary}")
    def increase_salary(self):
        self.salary = self.salary + ( self.salary * 0.10)
emp1 = Employee(1, "Ankit Rai", 30000)
emp1.show_emp_detail()
#_________print before increase in salary---------
print (emp1.show_emp_detail())
# ----------incresing salary-------
emp1.increase_salary()
#----after increaasing salary---------------
print(emp1.show_emp_detail())

Create an Employee class with a method that increases salary by 10%.



Python OOP Practice Questions (Beginner → Advanced) – 30 Questions---------------------------

Create an Employee class (name, age, salary), create two objects, and print their details.
Create a Book class (title, author, price), create three objects, and display details using a method.
Create a Car class (brand, model, year) and display details using a method.
Create a Student class (name, marks) with a method to check whether the student has passed (marks >= 40).
Create a Laptop class (brand, RAM) with a method to upgrade RAM by 8 GB.
Create a BankAccount class (account_holder, balance) with deposit(), withdraw(), and display_balance() methods.
Create a Mobile class (brand, model, price), modify the price after object creation, and display the updated value.
Create a Movie class (title, director, rating), delete one attribute after object creation, and print the object before and after deletion using __dict__.
Create any class of your choice and print all object attributes using __dict__.
Create five Employee objects, store them in a list, and print all employee names using a loop.
Create a Product class (name, price) with a method that returns the discounted price after applying a given discount percentage.
Create a Rectangle class with area() and perimeter() methods.
Create a Circle class with methods to calculate area and circumference.
Create a Customer class with a private balance attribute and access it using a getter method.
Extend Question 14 by adding a setter method to update the private balance.
Create an Employee class and a child class Manager with an additional department attribute using inheritance.
Create a Vehicle parent class and child classes Bike and Car that inherit from it.
Override a display() method in a child class so that the parent and child print different outputs (Polymorphism).
Create a Person class and a child class Teacher; use super() to initialize parent attributes.
Create an Employee class with a method that increases salary by 10%.
Create a SalesRecord class (product, quantity, price) with a total_sales() method.
Create an Employee class with an annual_salary() method.
Create a StudentMarks class that stores marks of five subjects and calculates average, highest, and lowest marks.
Create a SalesEmployee class that inherits from Employee, adds a sales attribute, and overrides the salary display method.
Create a Dataset class (rows, columns) with a dataset_info() method.
Create a CSVFile class with methods to open a CSV file and count its rows and columns.
Create a Report class with a generate_summary() method that prints total records, average value, and maximum value.
Create a BankTransaction class with a private balance attribute and methods deposit(), withdraw(), and check_balance().
Create a DataCleaner class with methods remove_null(), remove_duplicates(), and convert_datatype() (initially print messages; later implement using pandas).
Mini Project: Build an Employee Management System using OOP that supports adding, updating, deleting, searching, and displaying employees, calculating average salary, storing at least 10 employee objects, and demonstrates Classes, Objects, Constructors, Methods, Encapsulation, Inheritance, Polymorphism, super(), Private Attributes, and __dict__.