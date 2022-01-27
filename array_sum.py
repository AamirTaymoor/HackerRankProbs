#simple Array sum function
def arr_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
#demonstration
a = [12, 1, 2, 3, 5]
print(arr_sum(a))

