def printMax(input: list) -> int:
    max = 0
    for x in range(0, len(input)):
        if(input[x] > max):
            max = input[x]
    return max
# returns and prints 110
print(printMax([1, 9, 110, 5, 0 , -190]))
# returns and prints 999
print(printMax([999, -1, 3, 5, 10 , -1]))