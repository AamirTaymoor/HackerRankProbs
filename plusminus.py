def ratio(arr):
    p=0.0
    n=0.0
    z=0.0
    for i in arr:
        if(i > 0): p += 1
        elif(i < 0): n += 1
        elif(i == 0): z += 1
    p = p / len(arr)
    n = n / len(arr)
    z = z / len(arr)
    print('%.6f'%p)
    print('%.6f'%n)
    print('%.6f'%z)

#for demonstration
a = [1,2,3,0,0,-1,-1,0,-9]
ratio(a)
