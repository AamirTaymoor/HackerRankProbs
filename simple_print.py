#print the range of integers from 1 to input integer in the single line without a whitespace
#or newline
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')

    