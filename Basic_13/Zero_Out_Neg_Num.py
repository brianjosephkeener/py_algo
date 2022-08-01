def zero_out(input:list) -> list:
    for i in range(0, len(input)):
        if(input[i] < 0):
            input[i] = 0
    return input

print(zero_out([1, 10, -10, 5, 1]))