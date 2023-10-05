from itertools import combinations as cb

def solution(relation):
    rows = len(relation)        # rows: 데이터의 개수
    columns = len(relation[0])  # columns: 데이터 속성의 개수

    result = [] # result: 유일성을 만족하는 인덱스

    # 모든 인덱스의 조합에 대해 검사
    for r in range(1, columns + 1):
        for indices in cb(range(columns), r):
            # 유일성 검사
            a = set()
            for i in range(rows):
                a.add(tuple(relation[i][index] for index in indices))
                
            if len(a) != rows:
                continue
            
            # 최소성 검사
            for valid in result:
                if set(valid).issubset(set(indices)):
                    break
            else:  # for문에서 break되지 않는다면
                result.append(indices)

    return len(result)



# def solution(relation):
#     answer_list = list()
#     for i in range(1, 1 << len(relation[0])):
#         tmp_set = set()
#         for j in range(len(relation)):
#             tmp = ''
#             for k in range(len(relation[0])):
#                 if i & (1 << k):
#                     tmp += str(relation[j][k])
#             tmp_set.add(tmp)

#         if len(tmp_set) == len(relation):
#             not_duplicate = True
#             for num in answer_list:
#                 if (num & i) == num:
#                     not_duplicate = False
#                     break
#             if not_duplicate:
#                 answer_list.append(i)
#     return len(answer_list)