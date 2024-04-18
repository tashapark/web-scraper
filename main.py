# input은 하나의 argument만 받음. 유저가 답변을 해야 끝남. 엔터쳐야 함. 
# 뭐든지 치면 return에 저장 
# input은 이미 있는 built-in function

#비교를 위한 숫자로 변환
age = int(input("How old are you?"))

print("user answer", age)

# 형확인.
print(type(age))

# drink age calculator
if age < 18: 
    print("You can't drink.")
elif 18 <= age and age <= 35 : 
    print("You can drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
elif age == 19: 
    print("You are an adult! have fun!") 
else:
    print("Go ahead!")