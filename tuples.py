#this function creates a tuple from input data and calculates the hash function out of that
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    h = hash(t)
    print(h)