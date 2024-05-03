import random

ANSWER = random.randint(1, 20)
num_tries = 4

while 0 < num_tries:
    user = int(input(f"기회가 {num_tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
    if ANSWER == user:
      print(f"축하합니다. {num_tries}번 만에 숫자를 맞히셨습니다.")
      break
    elif ANSWER != user:
       if ANSWER > user:
          print("Up")
       elif ANSWER < user:
          print("Down")
    num_tries -=1

if num_tries ==0 :
        print(f"아쉽습니다. 정답은 {ANSWER}입니다.")


