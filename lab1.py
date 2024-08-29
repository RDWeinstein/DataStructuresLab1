#Using anything other than what we learned, please add a comment that explains what you are using and be able to answer it differently.
#Worth 5 points - due friday 8/30 before class. 5 points for a in-person quiz friday about similar tasks.

#1. Write a function reverse_and_uppercase(input_str) that takes a string, reverses it, and converts it to uppercase.
def reverse_and_uppercase(input_str):
    s = input_str[::-1]
    return s.upper()

assert reverse_and_uppercase("hello") == "OLLEH"
assert reverse_and_uppercase("DataStructures") == "SERUTCURTSATAD"

#2. Write a function basic_operations(a, b) that returns a tuple containing the sum, difference, product, and quotient of a and b.
def basic_operations(a, b):
    sum = a + b
    difference = a-b
    product = a*b
    quotient = a/b
    return (sum, difference, product, quotient)
    
assert basic_operations(10, 2) == (12, 8, 20, 5)

#3. Write a function check_sign(number) that returns "Positive", "Negative", or "Zero" based on the input number.
def check_sign(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'

assert check_sign(5) == "Positive"
assert check_sign(-3) == "Negative"
assert check_sign(0) == "Zero"

#4. Write a function sum_of_evens(numbers) that returns the sum of all even numbers in a list.
def sum_of_evens(numbers):
    total = 0
    for c in numbers:
        if c % 2 == 0:
            total += c
    return total 

assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12
assert sum_of_evens([7, 8, 9, 10]) == 18

#5. Write a recursive function fibonacci(n) that returns the nth Fibonacci number. Without recursion. Must use loop.
def fibonacci(n):
    if n <= 0:
        return 0
    num1 = 1
    num2 = 1
    for c in range(1, n-1, 1):
        temp = num2+num1
        num1 = num2
        num2 = temp
    return num2

assert fibonacci(5) == 5
assert fibonacci(10) == 55

#6. Write a function parse_and_calculate(expression) that takes a mathematical expression in string format (e.g., "3+5*2-4/2") and returns the result. Handle the operations with the correct order of precedence.
def parse_and_calculate(expression):
    i = 0
    while(i < len(expression)):
        if expression[i] == '*':
            a = int(expression[i-1])
            b = int(expression[i+1])
            product = a * b
            expression = expression[:i-1] + str(product) + expression[i+2:]
            i = 0
        elif expression[i] == '/':
            a = int(expression[i-1])
            b = int(expression[i+1])
            quot = a / b
            expression = expression[:i-1] + str(product) + expression[i+2:]
            i = 0
    sum = int(expression[0])
    expression = expression[1:]
    for i in range(1, len(expression)):
        if expression[i] == '+':
            b = int(expression[i+1])
            sum += b
        if expression[i] == '-':
            b = int(expression[i+1])
            sum -= b
    return(sum)

            
assert parse_and_calculate("3+5*2") == 13
assert parse_and_calculate("3+5*2-4/2") == 11
