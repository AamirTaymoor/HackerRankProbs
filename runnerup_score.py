#this function is used to find the runnerup score from the array of scores
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #l = list(arr)
    l = sorted(set(arr)) # to eliminate duplicate values
    print(l[-2])
