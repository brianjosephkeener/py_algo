def arrayWithOdds(input:int) -> list:
    result = []
    for x in range(0, input+1):
        if(x % 2 != 0):
            result.append(x)
    return result

print(arrayWithOdds(255))