def sumArray(arr):
    if len(arr) == 1:
        answer = arr[0]
        return answer
    else:
        arr[-2] += arr[-1]
        temp = arr.pop()
        return sumArray(arr)
        

myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sumArray(myArr))