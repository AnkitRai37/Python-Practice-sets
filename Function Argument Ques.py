#--1-
def multiply(a,b):
    result = a * b
    return result
print(multiply(4,5))

#--2-
def student_info(name, roll_no, course):
    return name, roll_no, course
print(student_info("Ankit", 37, "Btech"))

#--3-
def power(Base, Exponent=2):
    result = Base ** Exponent
    return result
print(power(3))

#---and---
def power(Base, Exponent=2):
    result = Base ** Exponent
    return result
print(power(3, 3))

#--4-
def function_book_detail(tittle, author_name, price):
    return tittle, author_name, price
print(function_book_detail(tittle = "The Lady", price = "250 USD", author_name = "Damon Bradly"))

#--5-
def Employee(name, age, department):
    return name, age, department
print(Employee(name = "Ankit", age = 22, department = "HR"))
print(Employee(name = "Ankit", department = "Data", age = 20))
print(Employee("Ankit", age =24, department = "IT"))
print(Employee("Ankit", 26, department = "Data"))
print(Employee("Ankit", 23, "Tech"))

#--6-
def average(*numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers)/len(numbers)
print(average(1,2,3,4,5,6,7,8,9,10))

#--7-
def  profile(**details):
    for key, value in details.items():#--.items() is especially useful when you need both key and value at the same time — for looping
        print(f"{key} : {value}")
profile(name = "Ankit", age = 20, city = "Delhi")
    
#-8-
def display_data(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} : {value}")
display_data(10, 20, 30, name = "Ankit", age = 25, city = "Lucknow")


#-9-
def shopping_list(item="Milk", *other_items):
    print("Default item :", item)
    for i in other_items:
        print("other_items:", i)
shopping_list()
shopping_list("Bread")
shopping_list("Jam", "Cake")
shopping_list("Jam", "Cake", "paties")

#-10-
def order_summary(customer, *items, **details):
    print("Order Summary")
    print("Customer:", customer)

    print("\nitem ordered:")
    for item in items:
        print("item:",item)

    print("\nitem details:")
    for key, value in details.items():
        print(f"{key} : {value}")
order_summary("Ankit", "Laptop", "Mouse", "Charger", gmail = "ankit@656856.com", contact = 65468765)

    Order Summary
Customer: Ankit

item:
item Laptop
item Mouse
item Charger

details:
gmail : ankit@656856.com
contact : 65468765





    











📝 Practice Questions
Required Arguments (Beginner)  
Write a function multiply(a, b) that takes two required arguments and returns their product. 
Call it with values 4 and 5.

Multiple Required Arguments (Beginner)  
Create a function student_info(name, roll_no, course) that prints student details. Call it with three arguments.

Default Arguments (Intermediate)  
Write a function power(base, exponent=2) that returns the result of raising base to the exponent.
 Test it with both one and two arguments.

Keyword Arguments (Intermediate)  
Define a function book_details(title, author, price) that prints book information. 
Call it using keyword arguments in different orders.

Mixing Positional and Keyword Arguments (Intermediate)  
Create a function employee(name, age, department) and call it using a mix of positional and keyword arguments.

Arbitrary Positional Arguments (args) (Intermediate)*
Write a function average(*numbers) that calculates and returns the average of any number of arguments passed.

Arbitrary Keyword Arguments (kwargs) (Intermediate)**
Create a function profile(**details) that prints all key-value pairs passed. 
Call it with arguments like name="Ankit", age=20, city="Lucknow".

**Combining *args and kwargs (Advanced)  
Write a function display_data(*args, **kwargs) that prints positional arguments first, 
then keyword arguments. Test it with multiple values.

*Default + args (Advanced)  
Create a function shopping_list(item="Milk", *other_items) that prints the default item and then all other items passed.
 Call it with different sets of arguments.

Complex Function (Advanced)  
Write a function order_summary(customer, *items, **details) where:
customer is required,
items are arbitrary positional arguments,
details are arbitrary keyword arguments (like address, payment_method).
Print a formatted summary of the order.



def order_summary(customer, *items, **details):
    print("Order Summary")
    print("Customer:", customer)

    print("\nItems Ordered:")
    for item in items:
        print("-", item)

    print("\nOrder Details:")
    for key, value in details.items():
        print(f"{key} : {value}")

# Example call
order_summary("Ankit", "Laptop", "Mouse", "Keyboard", address="Lucknow", payment_method="UPI")
