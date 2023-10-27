def safe() :
    f = int(c2) / m
    print(c1,"단의 안전율은", f, "입니다.")

All=[]
results = []
kg = []
v1 = input("바스켓의 하중을 입력하시오, 없다면 0을 입력하세요.") ##kg[0]
results.append(v1)
v2 = input("바스켓의 정격하중을 입력하시오, 없다면 0을 입력하세요.") ##kg[1]
results.append(v2)
e1 = input("승강기의 하중을 입력하시오, 없다면 0을 입력하세요.") ##kg[2]
results.append(e1)
e2 = input("승강기의 정격하중을 입력하시오, 없다면 0을 입력하세요.") ##kg[3]
results.append(e2)
b1 = input("1단붐 중량을 입력하시오.") ##kg[4]
results.append(b1)
b2 = input("2단붐 중량을 입력하시오, 없다면 0을 입력하세요.") ##kg[5]
results.append(b2)
b3 = input("3단붐 중량을 입력하시오, 없다면 0을 입력하세요.") ##kg[6]
results.append(b3)
b4 = input("4단붐 중량을 입력하시오, 없다면 0을 입력하세요.") ##kg[7]
results.append(b4)
b5 = input("5단붐 중량을 입력하시오, 없다면 0을 입력하세요.") ##kg[8]
results.append(b5)
b6 = input("6단붐 중량을 입력하시오, 없다면 0을 입력하세요.") ##kg[9]
results.append(b6)


for i in results :
    g = int(i)
    kg.append(g)


print("입력하신 데이터는 아래와 같습니다.")
print(kg)


w7 = kg[2] + kg[3]
w6 = kg[9] + kg[0] + kg[1]
w66 = w6 * 2
w5 = kg[8] + w66
w55 = w5 * 2
w4 = kg[7] + w55 - w6
w44 = w4 * 2
w3 = kg[6] + w44 - w5
w33 = w3 * 2
w2 = kg[5] + w33 - w4

c5 = 5
while c5 == 5 :
    c1 = input("몇단 와이어 및 체인의 안전율을 계산할까요? [ex)메인 : 메인 / 승강기 : 승강기 / 1~4단 = 1~4 / 종료 : 종료] ")
    if c1 == "종료" :
        break
    c2 = input("와이어 및 체인의 파단강도(kg)를 입력하세요")
    c3 = input("와이어 및 체인의 수를 입력하세요")

    if c1 == "4":
        m = w6 / int(c3)
        safe()
    elif c1 == "3" :
        m = w5 / int(c3)
        safe()
    elif c1 == "2" :
        m = w4 / int(c3)
        safe()
    elif c1 == "1" :
        m = w3 / int(c3)
        safe()
    elif c1 == "메인" :
        m = w2 / int(c3)
        safe()
    elif c1 == "승강기" :
        m = w7 / int(c3)
        safe()
    elif c1 == "전체" :
        m = w6 / int(c3)
        c1 = "4"
        safe()
        m = w5 / int(c3)
        c1 = "3"
        safe()
        m = w4 / int(c3)
        c1 = "2"
        safe()
        m = w3 / int(c3)
        c1 = "1"
        safe()
        m = w2 / int(c3)
        c1 = "메인"
        safe()






