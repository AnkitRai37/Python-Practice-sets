
for i in range(1,11):
    print(i)


x = 1
while x <= 10:
    print(x)
    x +=1


a = "ankitrai"
for i in range(8):
    print(a[i])


for i in range (2 ,21 ,2):
    print(i)


for i in range (5,51,5):
    print(i)


total = 0
for i in range(1, 101):   # goes from 1 to 100
    total += i
print("Sum is:", total)


n = 6
fact = 1
for i in range (1, n+1):
    fact = fact * i
    print ("your factorial no:",fact)


rev = ""
text = "hello world"
for char in text:
    rev = char + rev
print ("reversed:", rev)


text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


list1 = [1,24,765,9,0,5,4,7,54,3,6,3,6,]
for i in list1:
    print(i) 

for i in range(1,11):
    if i == 7:
        break
    else:
        print(i)

for i in range(1,11):
    if i % 2 != 0:
        continue
    else:
        print(i)     

count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("no is prime")
else:
    print("no is not prime")  

for num in range(1, 51):   # loop from 2 to 50
    is_prime = True        # assume number is prime
    for i in range(2, num):  # check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

a, b = 0, 1
for _ in range(10):   # loop 10 times
    print(a)
    a, b = b, a + b   # update values

for row in range(1,5):
    for col in range(row):
        print("*", end = " ") 
    print()       

for table in range(1,6):
    for i in range(1,11):
        print(table,"x", i, "=", table * i)
    print()    

num = 153
temp = num 
sum_of_cubes= 0
while temp > 0:
    digit = temp % 10 
    sum_of_cubes += digit ** 3    
    temp //= 10
if sum_of_cubes == num:
    print("no is armstrong")
else:
    print("no is not armstrong")    

numbers = [10, 25, 7, 99, 42]
max_val = numbers[0]
for lar_num in numbers:
    if lar_num > max_val:
        max_val = lar_num
print("Largest:", max_val) 

original = [1, 2, 2, 3, 4, 4, 5]
unique = []
for uni_val in original:
    if uni_val not in unique:
        unique.append(uni_val)
print("unique list:", unique)        

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
