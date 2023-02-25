# 문자열
T = int(input())

for _ in range(T):
    str1 = input()
    print(str1[0], str1[-1], sep='')
    
# sep= : 문자 사이에 뭐가 들어갈지 결정한다.
# end= : 한 줄에 출력되도록 한다.