from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    numbers_com = []
    # for문으로 랜덤으로 계속 숫자를 확인하게 
    for number_com in range(n): 
        numbers_com.append(randint(1, 45))
    return numbers_com

# def generate_numbers(n):
#     numbers = []

# while로도 가능함.
#     while len(numbers) < n:
#         num = randint(1, 45)
#         if num not in numbers:
#             numbers.append(num)

#     return numbers


def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    nums = generate_numbers(6)
    bonus_num = generate_numbers(1)[0]
    nums_sorted = sorted(nums)
    nums_sorted.append(bonus_num)
    return nums_sorted

#  훨씬 간단해짐.. 슬라이싱을 항상 머리 속에 넣고 있쟈....
# sort는 리스트 값을 반환하지 않고, sorted가 반환함.. none지옥에 빠지지 말자...
# def draw_winning_numbers(7):
#     return sorted(draw_winning_numbers[:6] + draw_winning_numbers[6:])

# 테스트 코드
print(draw_winning_numbers())