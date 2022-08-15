from typing import List
import sys
import array

def reverseArray(input: List[int]) -> List[int]:
    result = []
    for i in range(len(input) - 1, -1, -1):
        print(input[i])
        result.append(input[i])
    return result

# Given a numerical array, reverse the order of the
# values. The reversed array should have the same
# length, with existing elements moved to other
# indices so that the order of elements is reversed.

# print(reverseArray([1, 2, 3]))

# *************** #

def removeNeg(input: List[int]) -> List[int]:
    i = 0
    while(i < len(input)):
        print(input[i])
        if(input[i] < 0):
            input.pop(i)
        i+=1
    return input

# Implement a function removeNegatives()​ that
# accepts an array and removes any values that
# are less than zero.

# print(removeNeg([1, -2, 3])) | returns and then prints [1, 3]

# *************** #

def BinarySearch(input: List[int], target: int) -> bool:
    start = 0
    end = len(input) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(input[mid] > target):
            end = mid - 1
        elif(input[mid] < target):
            start = mid + 1
        else:
            return True
    return False

# print(BinarySearch([1, 2, 3, 5], 4)) | returns False
# print(BinarySearch([1, 2, 3, 5], 2)) | returns True

# Given a sorted array and a value, return whether
# that value is present in the array. Do not
# sequentially iterate the entire array. Instead,
# ‘divide and conquer’, taking advantage of the fact
# that the array is sorted.

# *************** #

def RotateArray(arr: List[int], shiftBy: int) -> List[int]:
    result = []
    if(shiftBy == 0):
        return arr
    elif(shiftBy > 0):
        while(shiftBy > 0):
            result.append(arr[shiftBy - len(arr) + 1])
            shiftBy-=1
        while(len(result) != len(arr)):
            result.append(arr[shiftBy])
            shiftBy+=1
        return result
    else:
        pass

# print(RotateArray([1, 2, 3], 1)) | returns [3,1,2]

# Implement rotateArr(arr, shiftBy)​ that
# accepts array and offset. Shift arr’s values to the
# right by that amount. ‘Wrap-around’ any values
# that shift off array’s end to the other side, so that
# no data is lost. Operate in-place: given
# ([1,2,3],1)​, change the array to [3,1,2]​.

# ***************************************# 

def Second2Last(input: List[int]) -> int:
    if(len(input) > 1):
        return input[len(input) - 2]
    else:
        return None

# print(Second2Last([1, 2, 3, 4, 5]))

# Return the second-to-last element of an array

# ***************************************# 

def Nth2Last(input: List[int], nth: int) -> int:
    return input[len(input) - nth - 1]

# print(Nth2Last([1,2,3,4,5], 1))

# Return the element that is N-from-array's end

# ***************************************# 

def SecondLargest(arr: List[int]) -> int:
    max = -999999999999999999999
    nth = max
    for i in range(0, len(arr)):
        if(arr[i] > max):
            nth = max
            max = arr[i]
    return nth

# print(SecondLargest([1, 2, 3, 4, 10, 100, 50, 99999]))

# Return the element that is 2nd largest in the array

# ***************************************# 

def NthLargest(arr: List[int], nth: int) -> int:
    arr = sorted(arr)
    print(arr)
    return arr[len(arr) - nth]
        
print(NthLargest([1, 2, 10, 18, -1, 0, -999, 1, 1000, 5], 3))
