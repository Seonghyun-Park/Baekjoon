# 오븐 시계
a, b = map(int, input().split())
c = int(input())
d = int((b + c) / 60) # 분을 시로 계산

if b + c < 60:
    print(a, b + c)
elif d >= 1:
    if a + d >= 24: # 24시가 넘어가면
        a = a - 24 # 0시부터 다시 시작
        print(a + d, (b + c) - (60 * d))
    else:
        print(a + d, (b + c) - (60 * d))