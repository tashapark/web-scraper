# 조건문

password_correct = False

if password_correct:
    print("Here is your money")
# else는 필요하면 써도 되고 아니면 안 써도 됨
else:
    print("Wrong password")


winner = 8

if winner > 10:
    print("Winner is greater than 10")
# elif 필요하면 계속 추가해도 됨. 
elif winner <10:
    print("Winner is less than 10")
else: 
    print("Winner is 10")