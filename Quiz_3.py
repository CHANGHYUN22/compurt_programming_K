person = {"달러": 1320, "엔": 950, "위안": 182}
a = [13, 200, 13]
b = person["달러"] * a[0]
c = person["엔"] * a[1]
d = person["위안"] * a[2]

print("철수가 가지고 있는 돈의 원화 가치는", b+c+d,"원 입니다.")
