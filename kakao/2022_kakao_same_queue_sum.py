from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    n = len(queue1)

    # 합이 큰 큐에서 작은 큐로 원소를 옮겨준다.

    a = sum(queue1)
    b = sum(queue2)
    answer = 0

    while True:
        if a > b:
            c = queue1.popleft()
            queue2.append(c)
            a -= c
            b += c
            answer += 1
        elif a < b:
            c = queue2.popleft()
            queue1.append(c)
            a += c
            b -= c
            answer += 1
        else:
            return answer
        if answer == n * 3:
            return -1
