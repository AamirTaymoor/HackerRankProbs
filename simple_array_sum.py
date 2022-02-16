from pandas import array


def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for a in ar:
        sum += a
    return sum
#demonstration
a= array([3,5,6,7,8])
print(simpleArraySum(a))