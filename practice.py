from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        nums = randint(1, 9)
        # 중복 값 제거 
        if nums not in numbers:
            numbers.append(nums)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    i = 1
    while i <= 3:
        num_guess = int(input(f"{i}번째 숫자를 입력하세요: "))
        if num_guess < 10 and num_guess > 0:
            if num_guess in new_guess:
                print("중복되는 숫자입니다. 다시 입력하세요.")
            # 다음 숫자로 안 넘어가고 다시 현재 숫자 입력 
                continue 
            new_guess.append(num_guess)
            i += 1
        else: 
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
            continue

# 이게 훨씬 더 간단함.
    # while len(new_guess) < 3:
    #     new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        
    #     if new_num < 0 or new_num > 9:
    #         print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    #     elif new_num in new_guess:
    #         print("중복되는 숫자입니다. 다시 입력하세요.")
    #     else:
    #         new_guess.append(new_num)

    return new_guess
    

 
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 여기에 코드를 작성하세요

    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        #조건문을 통과 못했으니깐, 위치가 이미 다르다는 것은 적용됨.  
        elif guesses[i] in solution:
            ball_count += 1
     
    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 여기에 코드를 작성하세요
while tries >= 0:
    guesses = take_guess()
    solution = ANSWER
    S, B = get_score(guesses, solution)
    print(f"{S}S", f"{B}B")
    if S != 3:
        tries += 1
    else:
        break

# argument 이름은 마음대로 해도 되니까 굳이.. solution으로 바꿔줄 필요 없고,
# if도 마지막에 1개만 쓰면 됨!!
# while True:
#     user_guess = take_guess()
#     s, b = get_score(user_guess, ANSWER)

#     print("{}S {}B\n".format(s, b))
#     tries += 1

#     if s == 3:
#         break
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))