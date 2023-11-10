import random

results = []
for i in range(6):
    number = random.randint(1, 45)
    results.append(number)

results.sort()
print(results)


if results in results_list :
    print('"',results_list, '"에 해당 숫자가 있습니다"')

if results not in results_list :
    print('"',results_list, '"에 해당 숫자가 없습니다"')


