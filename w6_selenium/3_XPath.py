# https://www.fun-coding.org/crawl_advance5.html

# Xpath = //태그이름[@속성='값']
'''
/ : 절대 경로
//: 문서 내에서 검색, 대부분 이 기능을 사용함
//@href: href 속성을 가진 모든 태그
//a[@href='http://google.com']: a태그의 href 값이 http://google.com인 모든 태그
//input[@type='password']: input태그의 type값이 password인 모든 태그
//*[@class='article']: class가 article인 모든 태그
(//a)[3]: 문서의 3번째 링크
(//table)[last()]: 문서의 마지막 테이블 선택
(//a)[position()<3]: 문서 처음 두 링크 선택
'''
# contains(): 속성 중 일부가 일치
# a[contains(@href,'naver')]: a 중 href 내부에 naver가 있는 태그 
# text()    : 내부 문자열 검사
# td[text()='UserID']       : td 중 내부 문자열이 UserID인 태그

