# 문자열 반복
T = int(input())

for _ in range(T):
    R, S = input().split() # 자료형이 다를 때는 그냥 input()을 쓰고 나중에 타입을 정해준다.
    
    for i in range(len(S)): # 문자의 길이만큼 반복
        print(S[i] * int(R), end='') # 반복해서 한줄에 출력
    print()
   