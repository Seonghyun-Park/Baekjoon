# 빠른 A+B
# 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 
# 시간초과가 발생할 수 있기 때문에 sys.stdin.readline() 을 사용해야 한다.
# sys.stdin.readline() 은 한줄 단위로 입력받는다.

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    
