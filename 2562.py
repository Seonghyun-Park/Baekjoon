# 최댓값
n_list = [] # 빈 배열 생성 = list()

for i in range(9):
    n_list.append(int(input())) # 반복할 때마다 확장하면서 배열에 입력한다.
    
print(max(n_list))
print(n_list.index(max(n_list)) + 1) # 처음을 1로 시작하기 때문에 +1