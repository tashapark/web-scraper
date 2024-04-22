class Puppy:
# method는 펑션 안에 있는 class
# class 안에 method를 가질 경우, 첫 번째 argument는 자동으로 self임.
# self 이외에 계속 업데이트 될 변수를 파라미터로 넣어줌. 
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

# self가 곧 루푸스임. 첫번째 argument라서 
# but, 밑에다가 bibi = Puppy()를 만들어도 출력은 계속 ruffus로 나옴
# 위에서 넣어준 파라미터 값을 함수에 추가 해주면 됨. 
# 위치 argument 사용 중임. 
ruffus = Puppy(
    "Ruffus", 
    "Beagle"
    )
bibi = Puppy(
    "Bibi", 
    "Dalmatian"
    )

print(ruffus.name, bibi.name)