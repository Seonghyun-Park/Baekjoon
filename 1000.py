a, b = input().split()

print(int(a) + int(b)) # input()함수는 기본적으로 문자형으로 취급하기 때문에 숫자는 형변환을 해주어야 한다.
print(int(a) - int(b))
print(int(a) * int(b))
print(int(int(a) / int(b)))
print(int(a) % int(b))