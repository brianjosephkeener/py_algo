import random
import sys

def Sigma(input: int) -> int:
    result = 0
    for i in range(1, input+1):
        result+=i
    return result

# Implement a function sigma(num)​ that, given a
# number, returns the sum of all positive integers
# from 1 up to number (inclusive)

# print(Sigma(3)) | returns 6
# print(Sigma(5)) | returns 15

# ********************* #

def Factorial(input: int) -> int:
    result = 1
    for i in range(1, input+1):
        result*=i
    return result

# Write a function factorial(num)​ that, given a
# number, returns the product (multiplication) of all
# positive integers from 1 up to number (inclusive).


# print(Factorial(3)) | returns 3
# print(Factorial(5)) | returns 120

# ********************* #

def Thr_A_Fiv():
    result = 0
    for i in range(100, 4000000):
        if(i % 3 == 0 and i % 5 == 0):
            continue
        else:
            if(i % 3 == 0):
                result+=i
                continue
            if(i % 5 == 0):
                result+=i
                continue
    print(result)


# Create function ThreesFives()​ that adds each value from 100 and 4000000 (inclusive) if that value
# is evenly divisible by 3 or 5 but not both. Display the final sum in the console.

# Thr_A_Fiv() prints answer: 3199999998000

# ********************* #

def generateCoinChange(input: int) -> None:
    coinage = {}
    coinage['Quarter'] = 0
    coinage['Dime'] = 0
    coinage['Nickel'] = 0
    coinage['Penny'] = 0
    while(input > 0):
        if(input >= 25):
            input-= 25
            coinage['Quarter'] = coinage.get('Quarter') + 1
        elif(input >= 10):
            input-= 10
            coinage['Dime'] = coinage.get('Dime') + 1
        elif(input >= 5):
            input-= 5
            coinage['Nickel'] = coinage.get('Nickel') + 1
        else:
            input-= 1
            coinage['Penny'] = coinage.get('Penny') + 1
    print(coinage)

# Implement generateCoinChange(cents)​ that accepts a parameter 
# for the number of cents, and computes how to represent that amount 
# with the smallest number of coins. print the result.

# generateCoinChange(97) prints {'Quarter': 3, 'Dime': 2, 'Nickel': 0, 'Penny': 2}
# generateCoinChange(50) prints {'Quarter': 2, 'Dime': 0, 'Nickel': 0, 'Penny': 0}

# ********************* #

def statisticToDouble():
    result = {
        "rolls": 0,
        "min": sys.maxsize,
        "max": -sys.maxsize,
        "average": 0
    }
    rolls = {
        "roll1": 0,
        "roll2": 0
    }

    while(True):
        rolls.update({"roll1": random.randint(1,6) })
        rolls.update({"roll2": random.randint(1,6) })
        if(rolls.get("roll1") == rolls.get("roll2")):
            if(result.get("rolls") == 0):
                result.update({"average": (rolls.get("roll1") + rolls.get("roll2"))})
                result.update({"min" : rolls.get("roll1") + rolls.get("roll2")})
                result.update({"max" : rolls.get("roll1") + rolls.get("roll2")})
                result.update({"rolls" : 1})
                break
            else:
                result.update({"average" : ((rolls.get("roll1") + rolls.get("roll2") + result.get("average")) / result.get("rolls"))})
                if(result.get("min") > rolls.get("roll1") + rolls.get("roll2")):
                    result.update({"min" : (rolls.get("roll1") + rolls.get("roll2"))})
                if(result.get("max") < rolls.get("roll1") + rolls.get("roll2")):
                    result.update({"max" : (rolls.get("roll1") + rolls.get("roll2"))})
                result.update({"rolls" : (result.get("rolls") + 1)})
                break
        else:
            result.update({"rolls" : (result.get("rolls") + 1)})
            result.update({"average" : result.get("average") + rolls.get("roll1") + rolls.get("roll2")})
            if(result.get("min") > rolls.get("roll1") + rolls.get("roll2")):
                result.update({"min" : (rolls.get("roll1") + rolls.get("roll2"))})
            if(result.get("max") < rolls.get("roll1") + rolls.get("roll2")):
                result.update({"max" : (rolls.get("roll1") + rolls.get("roll2"))})

    return result

# Implement a 'die' that randomly returns an integer between 1 and 6 inclusive.
# Roll a pair of these dice, tracking the statistics until doubles are rolled.
# Display the number of rolls, min, max and average.

# print(statisticToDouble()) | this return should be psuedo-random

# ********************* #

def Fibonacci(input:int) -> int:
    num1 = 0
    num2 = 1
    series = 0
    for i in range(input):
        print(series)
        num1 = num2
        num2 = series
        series = num1 + num2

# Implement the Fibonacci function, a famous mathematical equation that generates a numerical
# sequence such that each number is the sum of the previous two. 
# The Fibonacci numbers at index 0
# and 1, coincidentally, have values of 0 and 1. Your function should accept an argument of which
# Fibonacci number.
# Examples: fibonacci(2)​ = 1, fibonacci(3)​ = 2, fibonacci(4)​ = 3, fibonacci(5)​ = 5, etc.

# Fibonacci(5) - returns 0, 1, 1, 2, 3

# ********************* #

def DigitAB(num1:int, num2:int) -> int:
    original = num1
    for i in range(1, num2):
        print(num1)
        num1 = num1 * original
    return num1

print(DigitAB(12, 5))

# Implement a function that accepts two non-negative integers as arguments. Function lastDigitAtoB(a,
# b)​ should return the last digit of the first number (a) raised to an exponent of the second number (b).

# ********************* #


