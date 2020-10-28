print(1 == 1)
print(3 > 5)
print('-------')

a = '파이썬'
b = '파이선'
print(a == '파이썬')
print(a != b)
print('-------')

arr = ['파이썬', '자바스크립트', '루비', '고']
print(b in arr)
print(a not in arr)
print('-------')

if '자바' not in arr:
    arr.append('자바')
else:
    print('자바가 이미 존재합니다.')