# 중앙대학교 - 찬반투표
N = int(input())
vote = list(map(int, input().split())) # 배열로 입력 받는다.

approved = 0
rejected = 0
invalid = 0

for i in vote:
    if i == 1:
        approved += 1
    elif i == -1:
        rejected += 1
    elif i == 0:
        invalid += 1

if invalid >= approved + rejected:
    print('INVALID')      
elif approved > rejected:
    print('APPROVED')
elif rejected >= approved:
    print('REJECTED')
 