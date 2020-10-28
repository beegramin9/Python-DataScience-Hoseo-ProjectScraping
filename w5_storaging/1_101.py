'''
f = open('1_101.txt','a')

#   open('파일 이름','모드')
#   open 함수의 결과값(=파일)을 f라는 변수에 저장

f.write('I\'m excited to learn more!')
# 띄어쓰기 없이 바로 옆에 붙여서 써진다.
f.close()

# 모두 file의 타입 함수
'''

f = open('1_101.txt','r')
lines = f.readlines()
# 파일 내용을 줄별로 구분하여 리스트의 각 요소로 넣어 되돌려 줌
# 즉 lines[0], lines[1] 가능하고 반복문도 사용 가능
for line in lines:
    print(line)
f.close()
