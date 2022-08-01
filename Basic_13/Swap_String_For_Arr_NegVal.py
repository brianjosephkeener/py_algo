def ReplNegArr(input: list) -> list:
    for i in range(0, len(input)):
        if(input[i] < 0):
            input[i] = "Negative"
    return input

print(ReplNegArr([1, -1, 8, 0, -999]))