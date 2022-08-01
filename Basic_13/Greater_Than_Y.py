def Greater_Y(inputarr: list, y: int) -> list:
    result = []
    for i in range(0, len(inputarr)):
        if(inputarr[i] > y):
            result.append(inputarr[i])
    return result

print(Greater_Y([1, 5, 100, 78, -1, 0, -1000], 77))