numbers = [94, 23, 64, 39, 25, 10, 63, 6, 234, 34, 63, 4, 86, 5, 24, 1, 631, 90]

print(sorted(numbers))
# 파이썬의 내장 함수
# iterable의 값을 오름차순으로 정렬해 돌려주는 함수
print(numbers)
# 기존 iterable은 그대로, 건드리지 않는다.

alphabets = ['r', 'f', 'w', 'b', 'z', 'n', 'm', 'q', 'i', 'y', 'c']
print(sorted(alphabets))

words = ['coffee', 'car', 'carpet', 'candy', 'cure', 'crisis', 'cucumber']
print(sorted(words))
# 문자열은 사전순(lexicographic)으로 정렬, 한글도 가능

# mixed = [3, '호날두', 'Python', 15, '메시', 'Data']
# print(sorted(mixed))
# 문자열과 숫자형은 서로 정렬될 수 없음

# 딕셔너리에는 어떻게 적용될까?
scores = {'h': 16, 'b': 24, 'd': 91, 'c': 138, 'z': 6, 'a': 65}
print(sorted(scores))
# key를 기준으로 배열되어 리스트로 나온다.
# key,value값을 모두 포함하려면 .items함수를 사용하여 (key,value) 튜플로 만든 다음 옵션 선택

print(sorted(scores.items()))

def sortNum(item):
    return item[1]

print(sorted(scores.items(), key = sortNum))

# 원소 개수가 여러개인 튜플도 가능할까? 
three = [
    ('A',24,'M'),
    ('B',25,'F'),
    ('C',22,'F'),
    ('D',27,'M'),
    ('E',23,'M'),
    ('F',20,'F'),
    ('G',28,'M')
]

# def <정렬함수이름>(item):
#   return <item에서 정렬 기준으로 삼을 데이터>
# 
# print(sorted(Dictionary 변수.items(), key=정렬함수이름))

def sort1st(item):
    return item[1] # 정렬을 위해 비교되는 리스트의 요소, 이 경우에는 튜플
def sort2nd(item):
    return item[2]
def sort3rd(item):
    return item[3]

print(sorted(three, key = sort1st))
print(sorted(three, key = sort2nd))
print(sorted(three, key = sort3rd , reverse= True))

