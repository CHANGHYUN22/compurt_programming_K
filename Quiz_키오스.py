class Beverage :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    def calculate(self, quantity) :
        total_price = self.price * quantity
        print(f"{self.name}{quantity}잔의 가격은{total_price}원입니다.")


Coffee = Beverage("커피", 3000)
Greentea = Beverage("녹차", 2500)
Icetea = Beverage("아이스티", 3000)


a = 5
while a < 10 :
    selected_beverage = input("'커피', '녹차', '아이스티' 중 음료를 선택하세요 ")
    if selected_beverage in ["커피", "녹차", "아이스티"] :
        menu = input("몇 잔을 주문하시나요?: ")
        quantity = int(menu)
        if quantity > 0:
            if selected_beverage == "커피":
                Coffee.calculate(quantity)
                break
            elif selected_beverage == "녹차":
                Greentea.calculate(quantity)
                break
            elif selected_beverage == "아이스티":
                Icetea.calculate(quantity)
                break
        else:
            print("주문 수량이 잘못되었습니다.")
            print("처음부터 다시 선택해주세요")
    else:
        print("없는 메뉴입니다.")
        print("다시 선택해주세요")
