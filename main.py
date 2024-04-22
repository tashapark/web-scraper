class Puppy:
# 데이터 설정 setting하고. 파라미터 꼭 넣어주기.
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
#데이터 접근 access 가능 --> 프로퍼티 커스터 마이징 가능
    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

# ruffus, bibi는 puppy의 blueprint를 활용해서 만들어진 object로 instance임
ruffus = Puppy(
    name="Ruffus", 
    breed="Beagle"
    )
bibi = Puppy(
    name="Bibi", 
    breed="Dalmatian"
    )
# 하나씩 출력하는 게 아니라, 
# 전체를 출력하고 위에서 콘솔에 어떻게 보일지 property를 커스터 마이징 가능함 

print(bibi,
      ruffus,)