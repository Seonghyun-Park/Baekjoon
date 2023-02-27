# 단어 공부
word = input().upper() # 전체 문자를 대문자로 변환
word_list = list(set(word)) # set을 사용하여 중복된 문자 제거

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i))
    
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])