import random
sequence = 0

while True:
    number_player = int(input('1~10까지의 숫자 중 하나를 고르시오:'))
    number_computer = random.randint(1,10)
    if number_computer > number_player:
        sequence = 1
        print("컴퓨터는", number_computer, "을(를), 플레이어는", number_player, "(울)를 불렀습니다. 컴퓨터의 숫자가 더 높으므로 컴퓨터의 선공입니다.")
        break
    elif number_player > number_computer:
        sequence = 0
        print("컴퓨터는", number_computer, "을(를), 플레이어는", number_player, "(울)를 불렀습니다. 플레이어의 숫자가 더 높으므로 플레이어의 선공입니다.")
        break
    else:
        print("플레이어와 컴퓨터 모두 같은 숫자를 불렀습니다. 다시 숫자를 골라주세요.")