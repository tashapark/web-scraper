# 클래스로 코드가 안 날라다니게 할 수 있음. 
# 더 기능적임. 함수를 그냥 위로 안 쌓고 클래스에 넣으면 됨.
# property와 data를 완벽하게 캡슐화 함

# inheritance는 반복을 하지 않게 도와줌. 
# 부모로부터 다 받는 것.

class Dog:
     def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

     def sleep(self):
        print("zzzzzzzz..")

# (Dog)를 넣어주면 Dog를 전부 상속 받음.
#  Dog의 메소드 다 갖다가 쓸 수 있음.
class GuardDog(Dog):
 
    def __init__(self, name, breed):
        super().__init__(
            name, 
            breed, 
            3,
            )
        self.aggresive = True
        
    def rrrrr(self):
        print("stay away!")

# super().__init__ 부모 클래스를 참조하는 것 
# 변경되는 것은 값을 써주면 됨
#  당연히 부모에 포함되지 않는 것도 가질 수 있음. 
class Puppy(Dog):
    
    def __init__(self, name, breed):
        super().__init__(
            name, 
            breed, 
            0.1,
            )
        self.spoiled = True


    def woof_woof(self):
        print("Woof Woof!")


# ruffus, bibi는 puppy의 blueprint를 활용해서 만들어진 object로 instance임
ruffus = Puppy(
    name="Ruffus", 
    breed="Beagle"
    )
bibi = GuardDog(
    name="Bibi", 
    breed="Dalmatian"
    )
# 하나씩 출력하는 게 아니라, 
# 전체를 출력하고 위에서 콘솔에 어떻게 보일지 property를 커스터 마이징 가능함 

ruffus.sleep()
bibi.sleep()


