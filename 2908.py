# 상수
A, B = input().split()

A = int(A[::-1]) #문자열 A를 역순으로 출력해서 정수형으로 형변환 해준다.
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)