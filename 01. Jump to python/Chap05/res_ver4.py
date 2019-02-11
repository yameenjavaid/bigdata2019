class Restaurant :
    def __init__ (self, name, type, total) :
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = total
        self.todays_customer = total

    def describe_restaurant(self) :
        print ("저희 레스토랑 명칭은 [%s] 이고 [%s] 전문점입니다." %(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self) :
        print ("저희 [%s] 레스토랑 오픈했습니다. 어서오세요." %(self.restaurant_name))

    def reset_number_served(self, number):
        self.number_served = number
        print("손님 카운팅을 %s으로 초기화 하였습니다." %(self.number_served))

    def increment_number_served(self, number):
        self.number_served += number
        self.todays_customer += number
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다." %(number))

    def check_customer_number(self):
        print("지금까지 총 %s명 손님께서 오셨습니다." %(self.number_served))

    def __del__(self):
        print("이용해 주셔서 감사합니다.")

        f = open("고객서빙현황로그.txt", 'a')
        f.write('\n' + str(int(self.todays_customer)))
        f.close()


f = open("고객서빙현황로그.txt", 'w')
f.write('0')
f.close()

total = 0
f = open("고객서빙현황로그.txt", 'r')
line = f.read().splitlines()
for i in line:
    total = int(i)
f.close()

menu = input("레스토랑 이름과 요리 종류를 선택하시오.(공백으로 구분) : ").split(" ")
res = Restaurant(menu[0], menu[1], total)

res.describe_restaurant()
res.open_restaurant()

opening = input("레스토랑을 오픈하시겠습니까? (y/n) ")

if opening == 'y' :
    print("저희 %s 레스토랑이 오픈했습니다." %(res.restaurant_name))

    while True :
        choice = input("어서오세요. 몇명이십니까? (초기화:0, 종료:-1, 누적고객 확인:p)")

        if choice != 'p' :
            choice = int(choice)

        if choice == 0 :
            res.reset_number_served(0)
        elif choice == -1 :
            print("%s 레스토랑 문닫습니다." %(res.restaurant_name))
            exit()
        elif choice == 'p' :
            res.check_customer_number()
        else :
            res.increment_number_served(choice)

            f = open("고객서빙현황로그.txt", 'a')
            f.write('\n' + str(res.todays_customer))
            f.close()
