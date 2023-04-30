from collections import defaultdict

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    str1_elements = defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_elements[str1[0+i:2+i]] += 1

    str2_elements = defaultdict(int)
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_elements[str2[0+i:2+i]] += 1

    inter = {}
    
    for i, j in str1_elements.items():
        if i in str2_elements:
            inter[i] = min(j,str2_elements[i])

    union = str1_elements
    for element in str2_elements:
        if element in union:
            union[element] += str2_elements[element]
        else:
            union[element] = str2_elements[element]
    for i,j in inter.items():
        if i in union:
            union[i] -= j

    b = sum(union.values())
    a = sum(inter.values())
    
    if a==0 and b==0:
        answer = 65536
    else:
        answer = int(65536 * (a/b))

    return answer