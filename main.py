"""
built in이 아니면 python standard library에서 module을 import 해야 함
같은 모듈에서 여러 개는 ,로 가지고 오면 됨. 아래는 function만 쓰면 됨. 
 여러 줄을 주석 할 때는 "*3를 쓰면 됨. 앞 뒤에 
"""
# casino
from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1, 100)


playing = True

while playing:
    user_choice = int(input("Choose number (1-100):"))
    if user_choice == pc_choice:
        print("You won!!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")


# while은 control flow로 if와 같지만 멈추지 않음. if는 1번만 실행. 무조건 멈출 수 있는 값을 적용해야 함.

distance = 0

while distance < 20:
    print("I'm running:", distance, "km")
    # 0-19까지 해서 멈춤. 
    distance = distance + 1 


