# 평균
N = int(input())
n_list = list(map(int, input().split())) # 리스트로 입력받는다.
M = max(n_list)

new_list = [] # 새로운 성적을 담을 빈 리스트 생성
for score in n_list:
    new_list.append(score / M * 100) # 하나씩 확장하면서 추가한다.
    avg = sum(new_list) / N

print(avg)