#finding the absolute difference of the sum of elements of diagonals of a matrix
def diag_diff(m):
    d1 = 0
    d2 = 0
    for c in range(len(m),-1,-1):
            for r in range(len(m)):
                if((c + r) == len(m)-1):
                    d2 += m[r][c]
                if(r == c):
                    d1 += m[r][r]
    d_diff = d1-d2
    if d_diff <= 0:
        d_diff = -d_diff
    return d_diff
mat = [[3,6,8,3],[6,10,5,4],[7,4,2,1],[3,5,6,7]]
print(diag_diff(mat))
                


