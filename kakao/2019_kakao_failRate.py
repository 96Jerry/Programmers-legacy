N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# [3,4,2,1,5]

def solution(N, stages):
    fr = [-1]
    levels = [0] * (N+2)
    dict = {}
    

    for stage in stages:
        levels[stage] += 1
    total = sum(levels)
    for i in range(1,len(levels)):
        if total == 0:
            fr.append(0)
            continue
        fr.append(levels[i]/total)
        total -= levels[i]
    fr.pop()
    
    for i in range(len(fr)):
        dict[i] = fr[i]

    answer = sorted(dict,key=lambda x:dict[x],reverse=True)
    print(answer[:-1])

solution(N, stages)