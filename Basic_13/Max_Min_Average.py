

def Max_Min_Avg(input: list) -> list:
    max = -999999999999999999999
    min = 999999999999999999999
    average = 0
    result = []
    for i in range(0, len(input)):
        if(input[i] > max):
            max = input[i]
        if(input[i] < min):
            min = input[i]
        average+=input[i]
    average = average / len(input)
    result.append(max)
    result.append(min)
    result.append(average)
    return result

print(Max_Min_Avg([2, 3, 3, 5, 7, 10]))