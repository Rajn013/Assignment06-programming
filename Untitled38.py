#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[ ]:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i))


# 2.Write a Python Program to Find Factorial of Number Using Recursion?

# In[ ]:


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of", num, "is", factorial(num))


# 3.Write a Python Program to calculate your Body Mass Index?

# In[ ]:


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")


# 4.Write a Python Program to calculate the natural logarithm of any number?

# In[ ]:


import math
num = float(input("Enter a number: "))
ln = math.log(num)
print(f"The natural logarithm of {num} is {ln:.2f}")


# 5.Write a Python Program for cube sum of first n natural numbers?

# In[ ]:


n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i ** 3
print(f"The cube sum of the first {n} natural numbers is {sum}")


# In[ ]:




