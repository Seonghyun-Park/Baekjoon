# 공 넣기
N, M = map(int, input().split())
basket = [0] * (N + 1) # 가장 처음 바구니에는 공이 들어있지 않다.

for v in range(M):
    i, j, k = map(int, input().split())
    
    for n in range(i, j + 1): # i부터 j바구니까지
        basket[n] = k # 바구니에는 공을 1개만 넣을 수 있으므로 마지막에 들어온 k가 바구니의 공이다.

for ball_num in range(1, N + 1): # N개의 바구니에
    print(basket[ball_num], end=' ') # 마지막 공의 번호를 출력한다.
    