from random import randint


def generate_numbers():
    numbers = []

    # 여기에 코드를 작성하세요
    while len(numbers) < 3:
        nums = randint(1, 9)
        # 중복 값 제거 
        if nums not in numbers:
            numbers.append(nums)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
print(generate_numbers())

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


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
