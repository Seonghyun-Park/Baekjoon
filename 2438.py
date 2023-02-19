# 별 찍기 - 1
n = int(input())

for i in range(n):
    print('*' * (i + 1))
    
# 별 찍기 - 2
n = int(input())

for i in range(1, n + 1): # i가 1부터 5(6-1)까지
    print(" " * (n - i) + '*' * i)