def n_base(x, n):
    chars = '0123456789ABCDEF'
    answer = ''
    while x:
        x, remain = divmod(x, n)
        answer = chars[remain] + answer
    return answer or '0'

def solution(n, t, m, p):
    arr = ''.join(n_base(i, n) for i in range(t * m))
    return ''.join(arr[i*m+p-1] for i in range(t))


# def n_base(x,n):
#     # 61을 16진법으로 표현
#     # 61을 16으로 나눈 몫은 3, 나머지는 13
#     # 61: 3D
#     answer = ''
#     while x>=n:
#         remain = x%n
#         if remain == 10:
#             remain = 'A'
#         elif remain == 11:
#             remain = 'B'
#         elif remain == 12:
#             remain = 'C'
#         elif remain == 13:
#             remain = 'D'
#         elif remain == 14:
#             remain = 'E'
#         elif remain == 15:
#             remain = 'F'
        
#         answer = str(remain) + answer
#         x = x//n
#     if x == 10:
#         x = 'A'
#     elif x == 11:
#         x = 'B'
#     elif x == 12:
#         x = 'C'
#     elif x == 13:
#         x = 'D'
#     elif x == 14:
#         x = 'E'
#     elif x == 15:
#         x = 'F'
#     return str(x) + answer


# def solution(n, t, m, p):
#     # n: 진법, t: 구할 숫자의 갯수, m: 참가 인원, p: 튜브의 순서
    
#     # 2진법 0, 1
#     # 5진법 0,1,2,3,4
#     # ...
#     # 15진법 0, 1, 2, ..., A, B,C,D,E
#     # 16진법 0, 1, 2, ..., A,B,C,D,E,F
    
#     # 32 = 16 + 16 = 20(16진법)
#     # 31 = 16 + 15 = 1F(16진법)
#     # 61 = 16*3 + 13 = 3D(16진법)
    
#     # n: 16, t: 16, m: 2, p: 1
#     # 1. 리스트에 16=n진법으로 (1)부터 (구할 숫자의 갯수*참가인원)=t*m 까지 저장.
#     # 2. for문으로 참가인원=m 간격으로 돌면서 튜브의 순서=p에 있는 숫자를 구할 숫자의 갯수=t만큼 출력
#     # 2진법으로 숫자를 표현했을 때 arr의 길이가 100만 이하이려면
    
#     # arr: n진법으로 표현한 수의 리스트
#     arr = []
#     for i in range(100000):
#         arr.extend(n_base(i,n))
#         if len(arr) >= t*m:
#             break
            
#     answer = ''   
#     for i in range(100000):
#         answer += arr[m*i+p-1]
#         if len(answer) == t:
#             break
    
#     return answer