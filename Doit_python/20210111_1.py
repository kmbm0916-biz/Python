# 변수 생성 및 연산/출력
# a = 1 + 2
# b = 2 + 2
# c = 4 + 2
# print(a)

# 문자열 만들고 더해 연결
# head = "Python"
# tail = " is great lang"
# str = head + tail
# print(str)

# 문자열 곱하기
# a = "Python"
# print(a * 2)
# 응용>
# print("=" * 50)
# print("My Program")
# print("=" * 50)

# 문자열 인덱싱과 슬라이싱
#    0  .      1         2         3
#    0123456789012345678901234567890123
# a = "Life is too short, You need Python"
# print(a[3])

# 문자열 인덱싱 활용
# a = "Life is too short, You need Python"
# print(a[0]) # >> L
# print(a[12]) # >> a
# print(a[-1]) # >> n : 뒤에서부터 읽으려면 -를 붙인다.
# print(a[-0]) # >> L : == print(a[0])

# 단순 문자열 슬라이싱
# a = "Life is too short, You need Python"
# b = a[0] + a[1] + a[2] + a[3]
# print(b)

# 슬라이싱 기법 활용 문자열 슬라이싱 1
# a = "Life is too short, You need Python"
# b = a[0:4] # 인덱스 0번째 ~ 4번째까지 슬라이스
# print(b) # 위와 같은 결과(a[0] + a[1] + a[2] + a[3]).

# 슬라이싱 기법 활용 문자열 슬라이싱 2
# a = "Life is too short, You need Python"
# b = a[19:] # >> You need Python
# print(b) # == print(a[19:33])

# 슬라이싱 사용 예시 1
# a = "20010331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)
# print(weather)

# 슬라이싱 사용 예시 2
# a = "Pithon"
# print(a[:1] + 'y' + a[2:])

# 문자열 포맷팅
# print("I eat %d apples." % 3)
# %d = int %s = string %c = char %f = float %o = 8진수 %x = 16진수 %% = Literal(문자 '%', 이스케이프문 %)

# 2개 이상의 문자열 포맷팅
# print("I ate %d apples. So I was sick for %s days." % (10, "three"))

# 문자열 관련 함수
# count
# a = "hobby"
# print(a.count('b')) # >> 2 : 문자열 내부 b를 카운트
# find
# a = "Python is best choice"
# print(a.find('b')) # >> 10 : 문자열 내부 처음으로 나온 b의 인덱스 위치를 리턴. 없을경우 -1 리턴.
# index
# a = "Life is too short"
# print(a.index('t')) # >> 8 : find와 같이 처음 나온 문자 위치 리턴하나, 없을경우 오류 발생.
# print(a.index('k')) # >> Error
# join
# a = ","
# print(a.join('abcd')) # >> a,b,c,d : 문자열의 문자 사이에 변수 a의 값을 삽입.
# upper
# a = "hi"
# print(a.upper()) # >> HI : 문자열을 모두 대문자로 변경. 원본이 대문자인 경우 변화 없음.
# lower
# a = "HI"
# print(a.lower()) # >> hi : 문자열을 모두 소문자로 변경. 원본이 소문자인 경우 변화 없음.
# lstrip
# a = " hi "
# print(a.lstrip()) # >> hi  : 문자열 좌측의 공백을 모두 지운다.
# rstrip
# a = " hi "
# print(a.rstrip()) # >>  hi : 문자열 우측의 공백을 모두 지운다.
# strip
# a = "hi"
# print(a.strip()) # >> hi : 문자열 좌우의 공백을 모두 지운다.
# replace
# a = "Life is too short"
# print(a.replace("Life", "Your leg")) # >> Your leg too short : replace(바뀌게 될 문자열, 바꿀 문자열)
# split
# a = "Life is too short"
# print(a.split()) # >> ['Life', 'is', 'too', 'short'] : 공백을 기준으로 문자열을 나눔
# b = "a:b:c:d"
# print(b.split(":")) # >> ['a', 'b', 'c', 'd'] : 선택한 기호 기준으로 문자열을 나눔