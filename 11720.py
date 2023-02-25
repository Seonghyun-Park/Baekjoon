# 숫자의 합
N = int(input()) # 숫자의 개수
str1 = input()

sum1 = 0
for i in range(N): # 숫자의 개수가 주어지기 때문에 범위를 N으로 설정
    sum1 += int(str1[i])
print(sum1)