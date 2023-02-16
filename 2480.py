# 주사위 세개
a, b, c = map(int, input().split())

if a == b == c: # 세 수가 같을 때
    print(10000 + a * 1000)
elif a == b or a == c or b == c: # 두 수가 같을 때
    if a == b:
        print(1000 + a * 100)
    elif a == c:
        print(1000 + c * 100)
    elif b == c:
        print(1000 + b * 100)
else: # 세 수가 다를 때
    print(max(a, b, c) * 100) # max()는 최대값만 반환한다.
