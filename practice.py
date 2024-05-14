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



# 테스트 코드
print(generate_numbers(6))