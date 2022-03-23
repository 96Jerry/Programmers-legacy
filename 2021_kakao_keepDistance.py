from itertools import combinations as cb

places = [
    ["PPOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]
    ]
#result = [1, 0, 1, 1, 1]

def solution(places):

    ans = []

    for z in range(5):
        oneP = []
        oneX = []
        jud = []
        answer = 1

        # P 찾기
        for w in range(5):
            for i,j in enumerate(places[z][w]):
                if j =="P":
                    oneP.append((i,w))
        if oneP == []:
            ans.append(1)
            continue
        # X 찾기
        for w in range(5):
            for i,j in enumerate(places[z][w]):
                if j =="X":
                    oneX.append((i,w))
        
        # 거리 2 이하 P 찾기, 사이에 X 존재하는지 확인
        tmp=cb(oneP,2)
        if tmp:
            for i, j in tmp:
                if abs((i[0]-j[0]))+abs((i[1]-j[1])) == 1:
                    answer = 0
                    break
                if abs((i[0]-j[0]))+abs((i[1]-j[1])) == 2:
                    x = i[0] - j[0]
                    y = i[1] - j[1]
                    if oneX == []:
                        answer = 0
                        break
                    else:
                        if abs(x) == 2 or abs(y) == 2: 
                            if ((i[0]-x//2,i[1]-y//2) not in oneX):
                                answer = 0
                                break
                        else:
                            if ((i[0]-x,i[1]) not in oneX) or ((i[0],i[1]-y) not in oneX):
                                answer = 0
                                break
            ans.append(answer)
        else:
            ans.append(1)
        

    return ans

print(solution(places))