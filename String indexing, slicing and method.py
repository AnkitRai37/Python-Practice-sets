#  #-----String indexing-----

name = "Madhav"
print(name[4]) # normal indexing  and positive indexing---which starts from 0--

name = "Madhav"
print(name[-5]) #------negative indexing----which starts from (-1)--------

name = "Madhav Sharma"
print(name[6]) #---it give you space acc to your input --or blank space is also a char--          


#--string slicing ----


name = "Ankit Sharma"
print(name[0:7]) #---Its a  range----

name = "Ankit Rai"
print(name[0:7:1]) # start, end, step is used to get index--- find first 7 chars

name = "Ankit Rai"
print(name[0:7:2])

name = "Ankit Rai" # finding the len of the input---
print(len(name))

name = "Ankit Singh" #--its (-ve) slicing----, find last 5 char---
print(name[-1:-5:-2])


name = "Saurabh Rai"
print(name[4:6])

name = "Saurabh Rai"
print(name[4:6:2])  # ---find char bet 4 to 6 with 2 step----


name = "Saurabh Rai"
print(name[-5:]) #--last 5 chars----


# -- Reverse string---

name = "Saurabh Rai"
print(name[::-1])

##---String methods ---

#  1---len()---
string1 = "Hello Madahav"
print(len(string1))

#--2--Lower()--
string1 = "Hello Madahav"
print(string1.lower())

#--3--upper()--
string1 = "Hello Madahav"
print(string1.upper())

#--4--count()--
string1 = "Hello Madahav"
print(string1.count('a')) #---use to count, how mwnay times a char occur---

#--5--find()--
string1 = "Hello Madahav"
print(string1.find('h'))  #--its use to find the char index number---

#--6--split()--
string1 = "Hello, Madahav"
print(string1.split(',')) #--use to split the string based on separator----like (,) 

#---OR---
string1 = "Hello, Madahav"
print(string1.split())

#--7--replace()--
string1 = "Hello Abhishek"
print(string1.replace("Abhishek", "Keshav"))
#---print(string1.replace(old,new))



#--8--title()--
string1 = "Hello, Madahav, i have a family"
print(string1.title())#--use to covrt first char in upper case of each string---


#--9--strip()-----
string1 = "  Hello, Madahav    "
print(string1.strip()) #---use to remove unwantd spaces--


#--10--join()-----
string1 = "Hello", "Madahav", "Ankit"
print(" ".join(string1))

string1 = "Hello", "Madahav", "Ankit"
print("-".join(string1)) #---use to join string based on separator-----
