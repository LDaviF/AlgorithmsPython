def findHighest(arr):
    highest = arr[0]
    highestIndex = 0

    for i in range(len(arr)):
         if arr[i] > highest:
              highest = arr[i]
              highestIndex = i
    return highestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        highest = findHighest(arr)
        newArr.append(arr.pop(highest))
    return newArr

print(selectionSort([9, 3, 4, 5, 45, 0, 10, 6, 56]))