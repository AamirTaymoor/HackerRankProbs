def comp_triplets(a, b):
    """ this function compares the total points earned by a and b. details of problem is on the HackerRank website"""
    s = []
    ac = 0
    bc = 0
    for i in range(len(a)):
        if(a[i] > b[i]): ac += 1
        elif(a[i] < b[i]): bc += 1
    s.append(ac)
    s.append(bc)
    return s
#demonstration
a = [99, 45, 34]
b = [45, 56, 67]
score = comp_triplets(a, b)
print(score)
