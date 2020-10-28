# 가능한 key값: 변하지 않는 값. 그래서 튜플은 되지만 리스트는 안 됨
# 가능한 value값: 변하든 안 변하든 다 넣을 수 있음

# ---- dictionary 기본 구성 & 조회 ----

people = {'korean': 380, 'american': 42, 'japanese': 15}
people['german'] = 29
print(people)
print(people['korean'])
# ---- 중첩 dictionary 구조 ----

chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}

chnInfos['하트시그널2']['hit'] += 4500
chnInfos['하트시그널2']['like'] += 290

# 딕셔너리 타입 함수
# .keys(): 모든 key를 뽑아 dicts_keys로
# .values(): 모든 value를 뽑아 dicts_values 로
# .items(): (key,value) 튜플을 원소로 하는 dict_items 로
# iterable, 즉 리스트처럼 사용 가능하고 반복문에도 사용 가능

print(chnInfos.keys())
print(chnInfos.values())
print(chnInfos.items())

for item in people.items():
    print('There are',item[1],item[0],'people')