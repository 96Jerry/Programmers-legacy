from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
    ]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
    ]

# result = [1,1,1,1,2,4]

# First Solution
# def solution(info, query):

#     from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left

# def solution(information, queries):
#     answer = []
#     dic = defaultdict(list)
#     for info in information:
#         info = info.split()
#         condition = info[:-1]  
#         score = int(info[-1])
#         for i in range(5):
#             case = list(combinations([0,1,2,3], i))
#             for c in case:
#                 tmp = condition.copy()
#                 for idx in c:
#                     tmp[idx] = "-"
#                 key = ''.join(tmp)
#                 dic[key].append(score) 

#     for value in dic.values():
#         value.sort()   

#     for query in queries:
#         query = query.replace("and ", "")
#         query = query.split()
#         target_key = ''.join(query[:-1])
#         target_score = int(query[-1])
#         count = 0
#         if target_key in dic:
#             target_list = dic[target_key]
#             idx = bisect_left(target_list, target_score)
#             count = len(target_list) - idx
#         answer.append(count)      
#     return answer

# Second Solution
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a,b,c,d),list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[a,b,c,d].append(int(i[4]))

    for k in data:
        data[k].sort()
    
    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l) // 2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid + 1   
        answer.append(len(pool)-l)

    return answer





print(solution(info,query))