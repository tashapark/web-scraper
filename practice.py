from random import randint

# 로또 답 만들기 
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

# 정렬하고 보너스 점수 합해서 나타내기
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

# 유저 입력 값과 매치되는 지 확인하기 
def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    count = 0 
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count        
    

# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))