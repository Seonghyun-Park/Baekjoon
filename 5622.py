# 다이얼
alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 모여있는 알파벳들을 각각의 문자열로 만들어서 문자열을 원소로 하는 리스트 생성
word = input()
time = 0

for element in alpabet_list: # 리스트에서 각 원소를 꺼낸다.
    for i in element: # 리스트에서 꺼낸 각 원소를 한글자씩 분리한다.
        for j in word: # 입력받은 문자를 하나씩 분리한다.
            if i == j: # 두 알파벳이 같으면
                time += alpabet_list.index(element) + 3
                # 같은 알파벳이 있는 원소의 인덱스 번호에 3을 더해준다.
                # 2번 즉 'ABC'가 있는 위치까지 3초가 걸리기 때문
print(time)