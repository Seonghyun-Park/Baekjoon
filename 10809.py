# 알파벳 찾기
S = list(input()) # 입력받는 단어
alphabet = 'abcdefghijklmnopqrstuvwxyz' 

for i in alphabet:
    if i in S: # i번째에 해당하는 알파벳이 단어 S안에 있다면
        print(S.index(i), end=' ') # S 단어의 몇번째 인덱스인지 출력한다.
    else:
        print(-1, end=' ') # 단어에 없는 알파벳이라면 -1 출력
