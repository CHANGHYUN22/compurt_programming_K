z = input("주민등록번호 13자리를(-없이) 입력하세요) : ")
x = [2,3,4,5,6,7,8,9,2,3,4,5]
y = 0

for i in range(12) :
    sum = int(z[i] * x[i])
    y += sum
print(f'숫자를 모두 더한 겂은 {y}입니다')

x = (11 - (y % 11)) % 10

if int(z[-1]) == x:
    print("유효합니다")
else :
    print("유효하지 않습니다.")
