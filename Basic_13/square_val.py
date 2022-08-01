def squar_val(input:list) -> list:
    for i in range(0, len(input)):
        input[i] = input[i] * input[i]
    return input

print(squar_val([2, 8, 17, 94]))
