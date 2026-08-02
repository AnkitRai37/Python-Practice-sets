#--- String in python-------
#--String is written in single and double and triple quotes--

name = "Ankit"  #---Creating a string----
print(name)

#---Type checking----
print(type("Ankit"))

print('Ankit')  #---single quote--
print("Won't allow")
print("Ankit")  #---Double quotes---

print(''' "kw-double-Quotes" ''') #--want string with double quote--
print(" \"my world\" ")

#--Formatted string---
#--1=old style formatting ,  %-operator
name = "Ankit"
age = 20
print("my name is %s and %d" % (name, age)) #--%s and %D are the placeholders for string anh int

#--2-- str.format mrthod---
name = "Ankit"
age = 20
print("my name is {} and {}".format (name, age)) #--%s and %D are the placeholders for string anh int

#---wih refrence---
name = "Ankit"
age = 20
print("my name is {0} and {1}".format (name, age)) #--%s and %D are the placeholders for string anh int

name = "Ankit"
age = 20
print("my name is {1} and {0}".format (name, age)) #--%s and %D are the placeholders for string anh int

name = "Ankit"
age = 20
print("my name is {name} and {age}".format (name="Madhav", age=24)) #--%s and %D are the placeholders for string anh int

#--3--f-strings---
name = "Ankit"
age = 35
print(f"{name} {age}")

name = "Ankit"
age = 35
print(f"{name} {age+5}") # can add value in int--

#--Escape characters--- backslash(\) with chars
print(''' "kw-double-Quotes" ''') #--want string with double quote--

print(" \"my world\" ")
print(" \'my world\' ")

print(" my \n world ")

print(" hello\tworld ")


#---String operators----

a = "Hello"
b = "Python"
print(a+b) #--Concatinate
print(a*2) #--mutiple copies

#---MEMBERSHIP
a = "Hello" 
b = "Python"
if "H" in a:
    print("yes")
else:
    print("no")

#---Membership==
a = "Hello"
b = "Python"   
if "H" not in  a:
    print("yes")
else:
    print("no")

print("Hello\nworld")

print(r"Hello\nworld")  #--raw string---


name= "Hello"#---%--string---
name1 = 34  
print("the a %s and %d" % (name, name1))

