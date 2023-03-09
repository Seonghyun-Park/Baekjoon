# 행렬 덧셈
N, M = map(int, input().split())

A, B = [], []

for i in range(N):
    A.append(list(map(int, input().split()))) # 행렬 A를 입력받는다.
for i in range(N):
    B.append(list(map(int, input().split()))) # 행렬 B를 입력받는다.
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
        # 1행부터 각각의 열끼리 더하고 한 줄에 출력한 후
    print() # 한 행의 덧셈이 끝나면 한칸을 띄운다.