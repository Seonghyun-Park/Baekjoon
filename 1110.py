# 더하기 사이클
n = int(input()) # 26
num = n # 변하는 값
cycle = 0

while True:
    a = num // 10 # 2->6...   # // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 몫을 구함
    b = num % 10 # 6->8...
    c = (a + b) % 10 # 8->14...
    num = (b * 10) + c # 68->84...
    
    cycle += 1
    if num == n:
        break
    
print(cycle)