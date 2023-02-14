# 10430 : 나머지
a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# 2588 : 곱셈
a = int(input())
b = input()

sum3 = a * int(b[2])
sum4 = a * int(b[1])
sum5 = a * int(b[0])
sum6 = a * int(b)

print(sum3)
print(sum4)
print(sum5)
print(sum6)
