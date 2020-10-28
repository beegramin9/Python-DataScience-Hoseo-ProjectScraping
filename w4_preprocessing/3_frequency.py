subjects = ['파이썬', '자바스크립트', '루비', '코틀린', '자바스크립트', '파이썬',
            '파이썬', 'C++', 'iOS', '파이썬', 'Go', '안드로이드', '파이썬', '루비',
            'C++', 'iOS', '안드로이드', '파이썬', '파이썬', '자바스크립트', '루비',
            '안드로이드', '자바', '파이썬', '파이썬', 'C++', 'iOS', '파이썬',
            'Go', '자바', '파이썬', '루비', 'C++', 'iOS', '안드로이드', '파이썬']

output = {}

for subject in subjects:
    output[subject] = 0

print(output)

for subject in subjects:
    output[subject] += 1

print(output)