# ----Type of Function arguments---
#----1---Required argument----
def greeting(name):  #--name is a required parameter
    print("Hello,", name, "! Welcome to the world of Python.")
greeting("Ankit")#--Ankit i s a required argument which is passed to the function

#---with multiple parameter and argument----
def greeting(name, age):  #--name and age are required parameters
    print("Hello,", name, "! You are", age, "years old.")
greeting("Ankit", 20)#-- Ankit and 20 are required arguments which are passed to the function

#--2--Default argument----
def greeting(name = "Ankit"):  #--name is a required parameter
    print("Hello,", name, "! Welcome to the world of Python.")
greeting("Dheeraj")#--Dheeraj is a required argument which is passed to the function
greeting()#--Ankit is a default argument which is passed to the function

#---3--Keyword Argument---
def divide(a , b):  #--name and age are required parameters
    return a / b
result = divide(b = 5, a = 10)#--10 and 5 are keyword arguments which are passed to the function
print(result)
result = divide(10 , 20)#--10 and 20 are positional arguments which are passed to the function
print(result)


#--4-- Arbitrary Argument ----- or variable length argument
#---#-----POSITIONAL ARGUMENTS- -----
#------*args------
def addNum(*args):
    return sum(args)
result = addNum(1,3,6) #--variable no of argument---
print(result)

def addNum(*args):
    return type(args)  #---Tuple stored---
    return sum(args)
result = addNum(1,3,6)
print(result)

def greetings1(*names):
    for name in names:
        print("Hello,", name, "! Welcome to the world of Python.")
greetings1("Ankit", "Dheeraj", "Suresh")

#-----**KWARGS--------- arbitrary keyword argument--(**kwargs)
def show_data(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")
show_data(name="Ankit", age=20, city="New York")
