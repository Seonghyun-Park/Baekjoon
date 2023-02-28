# 단어 공부
word = input().upper() # 전체 문자를 대문자로 변환
word_list = list(set(word)) # set을 사용하여 중복된 문자 제거

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i)) # count 숫자를 리스트에 추가
    
if cnt.count(max(cnt)) > 1: # count 숫자 최댓값이 중복되면
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))]) # 최댓값의 인덱스