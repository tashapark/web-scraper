# list는 [] 메소드 사용 가능. mutable
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]

# method는 데이터 뒤에 결합/연결된 function
# index에 -1 넣으면 맨 뒤에서 부터 셈.tuple도 마찬가지
print(days_of_week[-4])


# Tuple은 () 만들면 변하지 않고 메소드 쓸 수 없음. immutable
days = ("Mon", "Tue", "Wed")
print(days[0])


#dicts {} key-value로 되어 있어서, 메소드 가능. mutable [index]가 아니어도 불러올 수 있음. 
player = {
    'name':'nico',
    'age': 12,
    'alive': True,
    'fav_food': ("🍕","🍔"),
    "friend": {
        "name": "lynn",
        'fav_food': ['🍎']
    }
}

print(player.get('age'))


# pop 지우기
player.pop('age')
# 데이터 추가 가능
player['xp'] = 1500

player['friend']['fav_food'].append("🍜")
print(player['friend'].get('fav_food'))
print(player.get('fav_food'))

# dic 안의 tuple은 업데이트로 덮어 쓸 수는 있지만, append는 안됨. 
# 즉 바뀌는 게 아님. 
player['fav_food'] = "🍎"
print(player['fav_food'])
