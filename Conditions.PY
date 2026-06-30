
a = 2
if a > 0:
    print("a is positive")

a = 16
if a / 2:
    print("a is even")
else:
    print("a is odd")

Marks = 40
if Marks >= 20 :
    print("pass")
else:   
    print("fail")

s = ""
if s :
    print("not empty")
else:
    print("empty")   

x = 20
if x >= 18:
    print("adult")
else:
    print("minor")

num = -3
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")        

distance_km = 50
if distance_km < 40:
    print("medium")
elif distance_km >= 40:
    print("large")
else:
    print ("small")     

marks = 80
if marks > 80:
    print("A")
elif marks >=70:
    print("B")
elif marks >=30:
    print("C")
else:
     print("D")

vowels = "i"
if vowels  in"aeiou":
    print("vowel")
else:
    print("consonant")

num = 10
if num % 2 == 0:
    print("divisible by 2")
elif num % 3 == 0:
    print("divisible by 3")
else:
    print("neither")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("weekend")
else:
    print("weekday")

year = 2000
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

month = 2
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June") 
elif month == 7:
    print("July")
elif month == 8:
    print ("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
else:
    print("December")

temp = 25
if temp < 0:
    print("Freezing")
elif temp <= 20:
    print("Cold")
elif temp  <= 35:
    print("warm")
else:
    print("Heat")

num = 8
if num % 2 == 0:
    print("Divisible by 2")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Neither")

time = 17
if time < 12 :
    print("Morning")
elif time < 14:
    print("Afternoon")
elif time <= 18:
    print("Evening")
else:
    print("Night")

password = "aeinkit123"
length = len(password)
if length <= 5:
    print("Weak")
elif length <=8:
    print ("Moderate")
else:
    print("Strong")

bmi = 25
if bmi < 18:
    print("underweight")
elif  bmi < 23:
    print("normal")
elif bmi <27:
    print("normal")
else:
     print("obese")

num = 15
if num <= 10:
    print("range 1-10")
elif num <= 20:
    print("range 11-20")
elif num <= 30:
    print("range 20-30")
else:
    print("greater than 30")

marks = 90
if marks >= 90:
    print("excellent")
elif marks >=70:
    print("good")
elif marks >= 500:
    print("average")
else:
    print("poor")
