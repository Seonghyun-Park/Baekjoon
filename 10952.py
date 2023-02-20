# A+B - 5
import sys

while True: # 무한 반복
    # a, b = map(int, input().split())
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a + b)
