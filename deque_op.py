""" this is solution to the collections.deque() problem of HackerRank python problem."""
from collections import deque

N = int(input("Enter the number of operations to be performed:"))
d = deque()
for _ in range(N):
    ops =list( input().split())
    if ops[0] == 'append':
        d.append(int(ops[1]))
    elif ops[0] == 'appendleft':
        d.appendleft(int(ops[1]))
    elif ops[0] == 'pop':
        d.pop()
    elif ops[0] =='popleft':
        d.popleft()
#for i in d:
    #print(i,end=" ")
print(*d)

        
