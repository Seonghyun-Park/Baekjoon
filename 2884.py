# 알람시계
h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
    
elif m < 45:
    if h == 0: # 0시에서 23시로 돌아간다.
        print(h + 23, m + 15)
    else:
        print(h - 1, m + 15)