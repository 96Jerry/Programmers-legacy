s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# result = [3, 2, 4, 1]

def guess(x):
    n = int((2*x)**0.5)
    return n

def solution(s):

    s = s[2:-2]
    tmpList = s.split("},{")
    # dictionary로 변환, {갯수 : 문자}
    dict = {}
    for i in range(len(tmpList)):
        tmpList[i] = tmpList[i].split(',')
        dict[len(tmpList[i])] = set(tmpList[i])

    answer = []
    answer.append([int(x) for x in dict[1]][0])
    for i in range(1,len(tmpList)):
        answer.append([int(x) for x in (dict[i+1] - dict[i])][0])

    return answer

print(solution(s))