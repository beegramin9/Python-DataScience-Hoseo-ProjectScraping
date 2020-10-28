import random
print(random.random())
# 0부터 1까지 숫자 중에서 아무 숫자나 뽑아서 돌려주는 것

print(random.randrange(1,6,2))
# range(start,stop,step) 함수로 만들어지는 정수 중 하나를 랜덤하게 선택

print(random.uniform(1,10))
# 두 숫자 사이의 랜덤 실수를 리턴 

print(random.randint(1,10))
# 두 숫자 사이의 랜덤 정수를 리턴 

abc = ['a','b','c','d','e']
random.shuffle(abc)
print(abc)
# 순서형 자료를 뒤죽박죽 섞어놓는 함수

print(random.choice(abc))
print(random.choice(abc))
# 순서형 자료의 원소를 아무거나 뽑아주는 함수

print(random.choice('abcdefg'))
# 랜덤하게 원소 하나를 선택



# example
print(random.choice([True,False]))
print(random.choice([True,False]))
# 참, 거짓 중 임의로 아무거나 뽑아주는 함수

# from random import random 으로 쓰면 더 편하다. 모두 다 random이 붙어있으니까
