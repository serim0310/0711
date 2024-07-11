# if - in - :
var = [1, 2, 3]

if 4 in var :
    print('OK')

else :
    print('NO')

# for - in - : 리스트 일 때
fruits = ["사과", "바나나", "딸기"]

for var in fruits :
    print("이는 첫번째", var)
    print("이는 두번째", var)
print("이는 for")

# for - in - : 딕셔너리 일 때
dic = {"봄" : "숭어", "여름" : "더움", "숫자" : 5}

for var in dic :
    print(var, dic[var])

# for - in - : 문자열 string
string = "오늘은 너무 덥네요. 빨리 집에 가고 싶어요."

for s in string :
    print(s)

# for - in - : 함수 range
for i in range(0, 10, 3) :
    print(i)

# while - :
# content = "사과"
#
# while content == "사과" :
#     print("OK")

# while 반복 멈추기
i = 10

while i < 100 :
    i = i + 1
    print("i는 지금 값이", i, "이므로, 100보다 작습니다.")

# while 반복 break
num = 0

while num < 1000 :
    num = num + 1
    if i == 500 :
        break
    print("대기번호 : ", num, "번")