p = "(())(())(())()()()()()()()()()()()(())))(("

def isgood(x):
    x = list(x)
    while 1:
        if x == []:
            return 1
        for i in range(len(x)):
            if x[i] == "(":
                if ')' in x:
                    index = x.index(")")
                else:
                    return 0
                del x[i]
                del x[index-1]
                break
            else:
                return 0

def seperate(x):
    if len(x) == 2:
        return x, ''
    for i in range(2, len(x)):
        a = x[:i]
        b = x[i:]
        if a.count('(') == a.count(')'):
            return a,b
    return x, ""
            
def reverse(x):
    x = x.replace("(",'3')
    x = x.replace(")","(")
    x = x.replace('3',")")
    return x

def solution(p):

    if p == "":
        return ""
    else:
        u,v = seperate(p)
        if isgood(u) == 1:
            return u + solution(v)
        else:
            empty = "("
            empty += solution(v)
            empty += ')'
            u = u[1:-1]
            empty += reverse(u)
            return empty


print(solution(p))