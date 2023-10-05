expression = "-10+20"
def seperate(x):

    tmp = ''
    dict = {}
    n = 0
    h = ''

    if x[0] == '-':
        h += '-'
        x = x[1:]

    for i in range(len(x)):
        if x[i].isdigit():
            tmp += x[i]
        else:
            # 이전 문자가 사칙연산기호면 tmp에 더해주는 것으로 끝
            if not x[i-1].isdigit():
                tmp += x[i]
            # 아니면 tmp를 dict에 추가시키고 사칙연산기호도 추가시킴
            else:
                dict[n] = tmp
                n += 1
                dict[n] = x[i]
                n += 1
                tmp = ''
    dict[n] = tmp
    if h:
        dict[0] = h + dict[0]
    return dict

def plus(x):
    # x 는 dictionary 자료형
    while '+' in x.values():
        for i,j in x.items():
            if j == '+':
                x[i-1] = str(int(x[i-1]) + int(x[i+1]))
                for z in range(i,len(x.keys())-2):
                    x[z] = x[z+2]
                y = sorted(x,reverse=True)
                for i in range(2):
                    del x[y[i]]
                break
    
    return x

def minus(x):
    # x 는 dictionary 자료형
    while '-' in x.values():
        for i,j in x.items():
            if j == '-':
                x[i-1] = str(int(x[i-1]) - int(x[i+1]))
                for z in range(i,len(x.keys())-2):
                    x[z] = x[z+2]
                y = sorted(x,reverse=True)
                for i in range(2):
                    del x[y[i]]
                break
    
    return x

def multiple(x):
    # x 는 dictionary 자료형
    while '*' in x.values():
        for i,j in x.items():
            if j == '*':
                x[i-1] = str(int(x[i-1]) * int(x[i+1]))
                for z in range(i,len(x.keys())-2):
                    x[z] = x[z+2]
                y = sorted(x,reverse=True)
                for i in range(2):
                    del x[y[i]]
                break
    
    return x
    
def one(ex):
    x = minus(plus(multiple(ex)))
    return abs(int(x[0]))

def two(ex):
    x = minus(multiple(plus(ex)))
    return abs(int(x[0]))
def three(ex):
    x = multiple(plus(minus(ex)))
    return abs(int(x[0]))
def four(ex):
    x = plus(minus(multiple(ex)))
    return abs(int(x[0]))
def five(ex):
    x = plus(multiple(minus(ex)))
    return abs(int(x[0]))
def six(ex):
    x = multiple(minus(plus(ex)))
    return abs(int(x[0]))



def solution(expression):
    e = expression
    one_ = seperate(e)
    two_ = seperate(e)
    three_ = seperate(e)
    four_ = seperate(e)
    five_ = seperate(e)
    six_ = seperate(e)
    answer = max(one(one_), two(two_), three(three_), four(four_), five(five_), six(six_))

    return answer

print(solution(expression))