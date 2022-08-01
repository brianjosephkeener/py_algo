def print_avg(input: list) -> int:
    global average
    average = 0
    for i in range(0, len(input)):
        average += input[i]
    average = average / len(input)
    return average

print(print_avg([2, 3, 3, 5, 7, 10]))