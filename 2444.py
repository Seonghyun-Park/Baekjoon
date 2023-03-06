# 별 찍기 - 7
N = int(input())

for i in range(1, N+1): 
    print(" " * (N-i) + '*' * (2*i-1)) # 윗부분 출력
for j in range(N-1, 0, -1): # for문의 범위를 거꾸로 할때는 step을 -1로 지정한다.
    print(" " * (N-j) + '*' * (2*j-1)) # 밑부분 출력