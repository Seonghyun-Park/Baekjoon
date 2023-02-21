# 개수 세기
n = int(input())

num_list = list(map(int, input().split()))
# list()로 선언하면 배열로 사용할 수 있다.

v = int(input())

print(num_list.count(v))
# count()는 배열 속에서 찾고자 하는 값이 몇 개 있는지 확인