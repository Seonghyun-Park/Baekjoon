# 그대로 출력하기
import sys

while True:
    try:
        print(input()) # 입력을 바로 출력한다.
    except EOFError: # EOF가 입력될 경우
        break
    
# 10951(A+B-4)는 입력을 숫자로만 받고
# 11718(그대로출력하기)는 입력이 알파벳 소문자, 대문자, 숫자, 공백으로 
# 이루어져 있기 때문에 except EOFError 를 사용했다.