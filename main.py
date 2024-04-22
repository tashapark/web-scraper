class Puppy:
# method는 펑션 안에 있는 class
# class 안에 method를 가질 경우, 첫 번째 argument는 자동으로 self임.
    def __init__(self):
        self.name = "Ruffus"
        self.age = 0.1
        self.breed = "Beagle"

# self가 곧 루푸스임. 첫번째 argument라서 
# but, 밑에다가 bibi = Puppy()를 만들어도 출력은 계속 ruffus로 나옴
ruffus = Puppy()

print(ruffus.name, ruffus.age, ruffus.breed)