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