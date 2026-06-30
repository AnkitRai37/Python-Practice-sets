def hello():
    print("Hello World!")
hello()

def add(a,b):
    return a + b
print(add(5,3))

def square(x):
    return x*x  
print(square(2))

def is_even(x):
    return x % 2 == 0
print(is_even(7))

def Greet(name):
    print("hello,", name)
Greet("Ankit")

def length_string(s):
    return(len(s))
print(length_string("ANKIT"))

def cel_to_far(c):
    return(9/5 * c) + 32
print(cel_to_far(25))

def absolute(num):
    return num if num >= 0 else -num 
print(absolute(-10))

def add_calculator(x, y):
    return x + y
print(add_calculator(3, 6))

def multipli_table(n):
    for i in range(1, 11):
        print(n, "x", "=", n*i)
multipli_table(7)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact  *= i
    return fact
print(factorial(4))

def is_prime(n):
    if n < 2 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
print(is_prime(19))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end = " ")
        a, b = b, a + b
fibonacci(10)
    
def rev_string(s):
    return s[::-1]
print(rev_string("hello"))

def sum_list(lst):
    return sum(lst)
print(sum_list([10, 26, 35, 29, 75]))

def largest_element(l):
    max_val = l[0]
    for i in l:
        if i > max_val:
            max_val = i
    return max_val
print(largest_element([10, 20, 37, 49,20, 96]))

def is_armstrong(n):
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total == n
print(is_armstrong(153))

def remove_duplicates(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return unique
print(remove_duplicates([1,2,3,2,4,1]))
    
def pattern_print(row):
    for row in range(1, row+1):
        for col in range(row):
            print("*", end = " ")
        print()
pattern_print(4)

def matrix_print(matrix):
    for row in matrix:
        for col in row:
            print(col, end = " ")
        print()
matrix_print ([[1,2,3],[4,5,6],[7,8,9]])

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n-1)
print(recursive_factorial(5))

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
print(recursive_fibonacci(8))

def is_palindrome(s):
    return s[ : :-1]
print(is_palindrome("malayalam"))

square = lambda x : x * x 
print(square(5))

def greet(name="Ankit"):
    print("Hello,", name)
greet()

def divide (a, b):
    quotient = a // b
    remainder = a % b
    return  quotient, remainder
q, r = divide(10, 3)
print("quotient:",q, "remainder:", r)

def square(x):
    return x*x
def area_of_square(side):
    return square(side)
print(area_of_square(5))

def grade_calculator(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
print(grade_calculator([85, 90, 78]))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello World"))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
def prime_in_range(limit):
    primes = []
    for i in range(2, limit+1):
        if is_prime(i):
            primes.append(i)
    return primes
print(prime_in_range(50))
