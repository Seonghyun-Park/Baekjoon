# 그룹 단어 체커
N = int(input())
count = 0

for _ in range(N):
    word = input()
    error = 0
    
    for i in range(len(word)-1): # 단어의 개수 - 1로 범위 설정
        if word[i] != word[i+1]: # 연속된 두 문자가 다르면
            new_word = word[i+1:] # 현재 글자 이후부터 새로운 문자열을 생성
            if new_word.count(word[i]) > 0: # 남아있는 문자열(새로운 문자열)에 현재글자가 있다면 
                error += 1 # 그룹단어가 아니다.
    if error == 0: # 그룹단어이다.
        count += 1

print(count) # 그룹단어의 수를 출력