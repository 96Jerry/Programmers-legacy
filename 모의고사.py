answers=[1,2,2,1,4]

def solution(answers):
        
    numbers=len(answers)
    
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*1250
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    a1=a[:numbers]
    b1=b[:numbers]
    c1=c[:numbers]

    cnt1=0
    cnt2=0
    cnt3=0

    for i in range(numbers):
        if answers[i]==a1[i]:
            cnt1+=1
    for i in range(numbers):
        if answers[i]==b1[i]:
            cnt2+=1
    for i in range(numbers):
        if answers[i]==c1[i]:
            cnt3+=1        

    cnt=[cnt1]+[cnt2]+[cnt3]
    something=sorted(list(enumerate(cnt,start=1)),key=lambda x:x[1],reverse=True)
    
    
    m=0
    answer=[]

    for i, j in something:
        if j>=m:
            m=j
            answer+=[i]



    return answer

print(solution(answers))
# why