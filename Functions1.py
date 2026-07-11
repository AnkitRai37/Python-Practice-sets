def greetings():
    print("Welcome to the python code by Ankit:,")
greetings() 

def add3numbers(a,b,c):
    result = a + b +c
    print("the three of two number is:", result )


add3numbers(b=28, a=43, 65)

# the return result statement #

def add2num(a,b):
    return a + b
#   return a-b # after 1st return statement function is end #
sum2num = add2num(3,5)
print(sum2num)

# fubction to convert celcius to fahrenheit
def Celsius_to_Fahrenheit(Celsius):
    Fahrenheit= (Celsius * 9/5) + 32
    return Fahrenheit
# call function
tempf = Celsius_to_Fahrenheit(25)
print(tempf)
print("with return:", type(tempf)) # return stmt gives value always
 #in data type which can you use on your further task#


# fubction to convert celcius to fahrenheit without return
def Celsius_to_Fahrenheit(Celsius):
    Fahrenheit= (Celsius * 9/5) + 32
    print(Fahrenheit)
# call function
tempf2 = Celsius_to_Fahrenheit(50)
print("without return:", type(tempf2)) # print stmt gives value always
 #in none type which can't you use on your further task#

 # thta is why wee need to use always return in functions#

# pass stmt

def kuchbhi():
    pass
#
print("Hello Wrold")

######################################

Common Logics to Remember
Fahrenheit Conversion

Code
Fahrenheit = (celsius * 9/5) + 32
👉 Multiply by 9, divide by 5, then add 32.

Palindrome Number

Reverse the number and compare with the original.

Code
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev == num → Palindrome
Armstrong Number

Sum of digits raised to the power of number of digits.

Code
digits_count = len(str(num))
sum_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_digits += digit ** digits_count
    temp //= 10
if sum_digits == num → Armstrong
Prime Number

Check divisibility from 2 to num-1 (or up to √num for efficiency).

Code
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime → Prime #

🔑 Programming Logic Cheat Sheet
Problem Type	Logic / Formula	Key Idea
Celsius → Fahrenheit	F = (C * 9/5) + 32	Multiply by 9, divide by 5, add 32
Fahrenheit → Celsius	C = (F - 32) * 5/9	Subtract 32, multiply by 5, divide by 9
Palindrome Number	Reverse digits → compare with original	rev = rev*10 + digit
Armstrong Number	Sum of digits^count	sum += digit ** digits_count
Prime Number	Check divisibility from 2 → √num	If divisible → not prime
Factorial	Multiply numbers from 1 → n	fact = fact * i
Fibonacci Series	next = a + b	Update: a = b, b = next
Sum of Digits	Extract digits with % 10, add	sum += digit
Reverse String	Loop backwards or slicing	s[::-1]
Greatest Common Divisor (GCD)	Euclidean algorithm	gcd(a,b) = gcd(b, a%b)
Least Common Multiple (LCM)	(a*b) / gcd(a,b)	Uses GCD
Even/Odd Check	num % 2 == 0	Remainder logic
Leap Year	(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)	Rule-based
List Sorted Check	Compare each element with next	If list[i] > list[i+1] → not sorted
Prime Factors	Divide repeatedly by smallest prime	Collect divisors
Binary Conversion	Divide by 2, store remainders	Reverse at end


###############################################

# 20 Practice Questions (Beginner → Advanced)
def say_hello():
    print("Hello, World!")
say_hello()


def hello_boy(name):
    print("hello,", name)
hello_boy("Ankit")


def add2numbers(a,b):
    result = a + b
    return result
add = add2numbers(4,6)
print(add)


def check_even_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
check_even_odd(17)


def cal_square(number):
    square = number ** 2
    return square
square_of_number = cal_square(5)
print(square_of_number)
  

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
num_factorial = factorial(5)
print(num_factorial)


def reverse_string(str):
    rev = ""
    for char in str:
        rev = char + rev
    return rev
string = reverse_string("Ankit")
print(string)


def count_vowels(str):
    count = 0
    vowels = "aeiouAEIOU" 
    for char in str:
        if char in vowels:
            count += 1
    return count  
result = count_vowels("Ankit")
print(result)


def str_palindrome(str):
    str = str.lower()
    rev = ""
    for char in str:
        rev = char + rev
    return rev == str
palindrome = str_palindrome("Naman")
print(palindrome)


def max_in_three_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
print(max_in_three_num(32,43,24))


def gen_fibonacci(n):
    fib_series = []
    a,b = 0,1
    while a <= n:
        fib_seriesappend(a)
        a, b=b, a+b
    return fib_series
print(gen_fibonacci(50))

# 2num
def gcd(a, b):
    while b != 0:
        a, b=b, a%b
    return a
print(gcd(56, 98))

# OR 3 num
def gcd_three(x, y, z):
    return gcd(gcd(x, y), z)
print(gcd_three(48, 18, 30)) 


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
print(lcm(12, 18))


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range (0, n - i - 1):
            if lst[j] > lst[j+1]:
                #swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
lst = [5,2,9,1,7]
print(bubble_sort(lst))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True
print(is_prime(2))


def frequency_string(str):
    str_freq = {}
    for char in str:
        if char in str_freq:
            str_freq[char] += 1
        else:
            str_freq[char] = 1
    return str_freq
print(frequency_string("Hello"))


def long_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
print(long_word("Python is a high level programming language"))
  
    
def remove_duplicate(lst):
    unique = []
    for duplicate in lst:
        if duplicate not in unique:
            unique.append(duplicate)
    return unique
print(remove_duplicate([12,54,7,4,10,4]))


def flatten_list(nested_list):
    flat =  []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat
print(flatten_list([1, [2 , 3], [4, [5, 6]], 7] ))


def calculate_sum(number):
    sum_of_digit = 0
    while n > 0:
        digit = item % 10
        sum_of_digit += digit
        number number // 10
    return sum_of_digit 
print(calculate_sum(34352353))






Beginner
Write a function to print "Hello, World!".

Write a function that takes a name and prints "Hello, <name>".

Write a function to add two numbers and return the result.

Write a function to check if a number is even or odd.

Write a function to calculate the square of a number.

🔹 Intermediate
Write a function to calculate factorial of a number.

Write a function to reverse a string.

Write a function to count vowels in a string.

Write a function to check if a string is palindrome.

Write a function to return the maximum of three numbers.

🔹 Advanced Practice
Write a function to generate Fibonacci series up to n.

Write a function to calculate GCD of two numbers.

Write a function to calculate LCM of two numbers.

Write a function to sort a list without using sort().

Write a function to check if a number is prime.

Write a function to count frequency of characters in a string.

Write a function to return longest word in a sentence.

Write a function to remove duplicates from a list.

Write a function to flatten a nested list.

Write a function to calculate sum of digits of a number.

🟢 HackerRank-Level (inside practice set)
HR1: Write a function to find the second largest number in a list.

HR2: Write a function to check if two strings are anagrams.

HR3: Write a function to calculate the average of numbers in a list.

HR4: Write a function to rotate a list by k positions.

HR5: Write a function to merge two sorted lists.

🔵 LeetCode-Level (inside practice set)
LC1: Write a function to implement binary search.

LC2: Write a function to check if parentheses are balanced.

LC3: Write a function to find two numbers in a list that add up to a target (Two Sum).

LC4: Write a function to remove duplicates from a sorted list.

LC5: Write a function to find the longest common prefix among strings.

