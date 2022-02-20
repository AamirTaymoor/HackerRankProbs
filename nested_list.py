#this function gives the list of second highest score names 
if __name__ == '__main__':
    s_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s_list.append([name, score])
    sec_high_score = sorted(set([score for name, 
    score in s_list]))[1]
    print('\n'.join(sorted([name for name,score in s_list if 
    score == sec_high_score])))