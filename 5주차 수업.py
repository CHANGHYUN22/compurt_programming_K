results = []
#matrix = [[1,2,3], [4,5,6], [7,8,9]]

#for row in matrix:
#    for element in row:
#        if element%2 == 0:
#           results.append(element)
#print(results)

pingpong_list = ["나영", "예진", "원빈", "현빈"]


def create_contents_of_mail(XX):
    contents = "“한국교통대학교 천하제일 탁구대회," + XX + "님 탁구 대회에 참여해주셔서 감사합니다. 행사 일시: 2023-10-06, 시간: 10:30 AM, 복장: 트레이닝 복장 행사 당일에 뵙겠습니다." + XX + "님 감사합니다.”"
    return contents

for i in pingpong_list:
    #print(create_contents_of_mail(i))
    results.append(create_contents_of_mail(i))

print(results)
