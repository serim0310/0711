# 연습문제 10
i = 0
y = []#홀수값을 리스트로 저장

while i < 100 :
    i = i + 1
    if i % 2 == 1 :
        y.append(i)#홀수값 도출

print(sum(y))