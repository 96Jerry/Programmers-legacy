def solution(rows, columns, queries):
    # for query in queries
    # query에 대해 (x1,y1),(x2,y2) => (x1,y1) 부터 (x2,y1) 까지, 해서 총 4개의 직사각형 변을 확인. 각 꼭지점은 빼고,
    # 나중에 더해줌
    # 그리고 제일 작은걸 result에 append.
    # 시계방향으로 회전 => 값을 시계방향 순서대로 리스트에 저장해놨다가 그 위치를 비우고 다시 정렬
    
    # 2차원배열 arr 만들어주기
    arr = []
    for j in range(1, rows+1):
        arr_in = []
        for i in range(columns*(j-1)+1, columns*j+1):
            arr_in.append(i)
        arr.append(arr_in)
        
    result = []
    
    for query in queries:
        temp = []
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        # 시계방향으로 돌면서 정보 저장, 0으로 초기화
        for i in range(y1,y2):
            temp.append(arr[x1][i])
            arr[x1][i] = 0
        for j in range(x1,x2):
            temp.append(arr[j][y2])
            arr[j][y2] = 0
        for k in range(y2,y1,-1):
            temp.append(arr[x2][k])
            arr[x2][k] = 0
        for l in range(x2,x1,-1):
            temp.append(arr[l][y1])
            arr[l][y1] = 0    
        result.append(min(temp))
        # 시계방향으로 돌면서 값을 다르게 저장
        a = temp.pop()
        temp.insert(0,a)
        for i in range(y1,y2):            
            arr[x1][i] = temp.pop(0)
        for j in range(x1,x2):    
            arr[j][y2] = temp.pop(0)
        for k in range(y2,y1,-1):
            arr[x2][k] = temp.pop(0)
        for l in range(x2,x1,-1):
            arr[l][y1] = temp.pop(0)
        
        
    return result