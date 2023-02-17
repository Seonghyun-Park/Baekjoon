# 알람시계
h, m = map(int, input().split())

if m >= 45: # 45분이 지났을 때
    print(h, m - 45)
    
elif m < 45: # 45분이 지나지 않았을 때
    if h == 0: # 0시에서 23시로 돌아간다.
        print(h + 23, m + 15)
    else:
        print(h - 1, m + 15)
