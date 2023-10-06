def 구구단(a):
    for x in range(1, a):
        print("------["+str(x)+"단]------")
        for y in range(1, a):
            print(x, "X", y, "=", x*y)

b = input("몇 단까지 출력할까요")
구구단(int(b)+1)
