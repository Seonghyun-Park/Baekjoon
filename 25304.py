# 영수증
x = int(input())
n = int(input())
sum1 = 0 # 0으로 초기화

for i in range(n):
    a, b = map(int, input().split())
    sum1 += a * b # a*b의 값을 누적시킨다.

if x == sum1:
    print('Yes')
else:
    print('No')