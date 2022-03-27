n = 1
k = 3
# result = 3

def trans(n,k):
    x = []
    while n >= k:
        x.append(str(n % k))
        n = n // k
    x.append(str(n%k))
    x.reverse()
    x = ''.join(x)
    return x

def isPrime(x):
    if x <= 3:
        if x == 2 or x == 3:
            return 1
        else:
            return 0
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1

def solution(n,k):
    y = trans(n,k)

    if '0' not in y:
        return isPrime(int(y))
    
    answer = 0
    z = y.split('0')

    for i in z:
        if i:
            if isPrime(int(i)) == 1:
                answer += 1
    return answer

print(solution(n,k))