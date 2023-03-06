# 팰린드롬인지 확인하기
word = input()

if word == word[::-1]: # 문자열과 거꾸로 반복한 문자열이 같다면
    print('1')
else:
    print('0')