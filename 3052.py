# 나머지
n_list = []
for _ in range(10):
    n = int(input()) # 그냥 정수로 일단 n에 저장
    n_list.append(n % 42) # n을 42로 나눈 값을 n_list에 저장
    
n_list = set(n_list) # set(집합) 함수를 사용하여 중복을 없앤다.
print(len(n_list)) # 중복을 제거한 길이를 출력한다.

# 배열(list) - 순서 O, 중복 O
# 집합(set) - 순서 X, 중복 X