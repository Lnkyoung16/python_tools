import random

computer_temporary = []
player_temporary = []

def check_overlap(list1, list2, card):
    total_list = list1 + list2
    for i in range(0, len(total_list)):
        if card == total_list[i]:
            return 0

def new_card_generator():
    temporary = []
    while len(temporary) != 1:
        card_number = random.randint(0, 12)
        card_shape = random.randint(0, 3)
        if card_shape == 0:
            card_shape = "♠︎"
        elif card_shape == 1:
            card_shape = "♣"
        elif card_shape == 2:
            card_shape = "♥"
        else:
            card_shape = "♦"
        card = card_shape + str(card_number)
        overlap = check_overlap(player_temporary, computer_temporary, card)
        if overlap != 0:
            return card

print(new_card_generator())