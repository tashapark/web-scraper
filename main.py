def tax_calc(money):
# print를 리턴으로 바꾸면, 결과 값을 코드 상에 저장하는 것임.
# 그러면 당연히 콘솔에는 안보임. so, 값을 코드에서 다시 쓸 때 return 사용
   return(money * 0.35)

def pay_tax(tax):
    print("thank you for paying", tax)

# to_pay = tax_calc(150000000) 
# pay_tax(to_pay)변수 안 만들고 간단히 안에 함수를 넣어도 됨
pay_tax(tax_calc(150000000))


my_name = "nico"
my_age = 12
my_color_eyes = "brown"

# 변수를 포함한 string 만들기 f""안에 {변수명} 넣으면 됨. 
# 백틱이랑 달리 엔터치면 끊김
print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")

# juice maker.. 
def make_juice(fruit):
    # return은 함수 값을 밖으로 던지지만, 파이썬이 잡아서 코드에 넣어줌. 
    # return은 함수를 끝냄. 보이면 끝남. 
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)