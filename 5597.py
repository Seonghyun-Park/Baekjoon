# 과제 안 내신 분..?
student = [i for i in range(1, 31)] # 1번부터 30번까지 출석번호

for _ in range(28): # 총 28번의 입력
    n = int(input())
    student.remove(n) # n에 해당하는 숫자를 student 리스트에서 지운다.

print(min(student))
print(max(student))