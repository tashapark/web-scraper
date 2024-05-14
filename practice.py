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
    count = 0 
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count        
    
# 번호 확인해서 당첨금 제시하기 
def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    if count_matching_numbers(numbers, winning_numbers) == 6:
        if numbers[0:] == winning_numbers[:6]:
            return 10000000000
        else:
            return 500000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3:
        return 5000
    else:
        print("take a rain check :(")
        
        
# 이렇게 변수명 지정하면 중복 길이를 줄일 수 있음. 
# def check(numbers, winning_numbers):
#     count = count_matching_numbers(numbers, winning_numbers[:6])
#     bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

#     if count == 6:
#         return 1000000000
#     elif count == 5 and bonus_count == 1:
#         return 50000000
#     elif count == 5:
#         return 1000000
#     elif count == 4:
#         return 50000
#     elif count == 3:
#         return 5000
#     else:
#         return 0

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))