word = []
length = []

for i in range(5):
    word.append(input()) # 배열에 문자열을 담는다.
    length.append(len(word[i])) # word가 배열이니까 배열의 각 인덱스(문자열)의 길이
    

vertical_word = ''
for col in range(max(length)): # 열의 최대 길이
    for row in range(5): # 행의 길이 
        if col < length[row]: # 열의 길이가 행의 길이보다 작으면
            vertical_word += word[row][col] # 그냥 뛰어넘는다.

print(vertical_word)