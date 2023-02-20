# A+B - 4
import sys

while True: # 무한 반복
    try: # 에러가 발생할 여지가 있는 문장을 try구문으로 작성
        a, b = map(int, input().split())
        print(a + b)
    except: # 에러 발생 시 실행시킬 문장 작성
        break
    
# 반복문이 끝나는 조건이 주어지지 않았으므로 에러가 발생하면 반복문을 끝내도록 try-except구문을 활용

# try-except-else-finally -> 예외 처리
# try 구문 쪽에 에러가 발생할 가능성이 있는 코드를 작성하고
# except 구문 쪽에 예외 발생 시 실행할 코드를 작성
# else 구문에는 에러가 발생하지 않았을 때 실행할 문장을 작성
# finally 구문에는 무조건 실행할 코드를 작성