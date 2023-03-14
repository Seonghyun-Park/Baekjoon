# 최댓값 - 2차원 배열
import sys
input = sys.stdin.readline # 여러 줄을 입력받을 때는 이 형식을 사용한다.

A = []

for i in range(9):
    A.append(list(map(int, input().split()))) # 행렬 입력

row = 0
col = 0
Max = -1

for i in range(9):
    for j in range(9):
        if A[i][j] > Max:
            Max = A[i][j] # 최댓값 설정
            row = i+1 # 0부터 시작해서 +1
            col = j+1

print(Max)
print(row, col)
            