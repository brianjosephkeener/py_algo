def shift_arr(input: list) -> list:
    global result
    result = []
    for i in range(1, len(input)):
        result.append(input[i])
    result.append(0)
    return result

print(shift_arr([1, 2, 3, 4]))