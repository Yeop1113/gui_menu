import time
import random

menulist = ['짜장면', '짬뽕', '탕슉', '라면', '국밥']

print("골라줘 메뉴!")
print("AI가 추천해준 메뉴는?")
for i in range(5, 0, -1):
    print(i,"..")
    time.sleep(1)
# print("4..")
# time.sleep(1)
# print("3..")
# time.sleep(1)
# print("2..")
# time.sleep(1)
# print("1..")
print("오늘의 추천 메뉴는?")
menu = random.choice(menulist)
print(f'{menu} 입니다.')