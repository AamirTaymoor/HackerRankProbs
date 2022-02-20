#function for printing the cartesian product of two iterables using itertools.product function
from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int,B))
output = list(product(A,B))
for i in output:
    print(i, end=' ')