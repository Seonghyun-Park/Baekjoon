# 바구니 뒤집기
N, M = map(int, input().split())
basket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
    # [::-1] : 처음부터 끝까지 역순으로

print(*basket)    
