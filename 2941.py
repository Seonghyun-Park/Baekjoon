croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia_list: # croatia_list를 반복
    word = word.replace(i, '*') # input 변수와 동일한 이름의 변수
    # word에 croatia_list안에 있는 알파벳을 찾아서 '*'로 바꾼다.
    # print(word) # 과정 참고
print(len(word))

# replace() 함수를 문자열 원형이 변형되도록 사용하려면 입력받은 변수와
# 동일한 이름으로 변수를 지정하여야 for문을 반복하는 동안 수정된 내용이 for문 끝날 때까지 유지될 수 있다.