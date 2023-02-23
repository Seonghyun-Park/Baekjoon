# 공 바꾸기
N, M = map(int, input().split())
basket = [str(i+1) for i in range(N)]
# 1번부터 N번 바구니에 있는 공의 번호를 저장하는 리스트 선언

for exchange in range(M): # M번 교환
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] # 원소 교환
    # basket의 i-1번째에 j-1번째를 넣고, j-1번째에 i-1번째를 넣는다.
print(*basket) # 언팩킹 -> 리스트 형태를 풀어서 출력한다. -> 3 1 4 2 5
# print(basket) # 팩킹 -> ['3', '1', '4', '2', '5']

# 리스트 안에서 for문 사용하기
# [ 표현식 for 항목 in 리스트 or 튜플 ]
# [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]

# 파이썬 리스트 두 원소 위치 교체
# ex)
# array = [1,2,3,4,5]

# # 교체
# array[0], array[3] = array[3], array[0]
# # array의 0번째 원소에 3번째 원소를 넣고, 3번째 원소에 0번째 원소를 넣는다.

# print(array) # [4,2,3,1,5]