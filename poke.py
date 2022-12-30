import random
import re

all_card = ['m1', 'm2', 'm3', "m4", 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13',
            's1', 's2', 's3', "s4", 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13',
            'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13',
            'b1', 'b2', 'b3', "b4", 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13'
            ]

my_sym = []
my_num = []
my_card = []
for i in range(1, 4):
    num = all_card[random.randint(0, 51)]
    split_sym = re.search("[a-z]", num).group()
    split_num = int(re.search("\d+", num).group())
    my_sym.append(split_sym)
    my_num.append(int(split_num))
    if 1 < split_num <= 10:
        if split_sym == "m":
            my_card.append(f"♣{split_num}")
        elif split_sym == "s":
            my_card.append(f"♦{split_num}")
        elif split_sym == "r":
            my_card.append(f"♥{split_num}")
        elif split_sym == "b":
            my_card.append(f"♠{split_num}")
    else:
        if split_num == 1:
            if split_sym == "m":
                my_card.append(f"♣A")
            elif split_sym == "s":
                my_card.append(f"♦A")
            elif split_sym == "r":
                my_card.append(f"♥A")
            elif split_sym == "b":
                my_card.append(f"♠A")
        elif split_num == 11:
            if split_sym == "m":
                my_card.append(f"♣J")
            elif split_sym == "s":
                my_card.append(f"♦J")
            elif split_sym == "r":
                my_card.append(f"♥J")
            elif split_sym == "b":
                my_card.append(f"♠J")
        elif split_num == 12:
            if split_sym == "m":
                my_card.append(f"♣Q")
            elif split_sym == "s":
                my_card.append(f"♦Q")
            elif split_sym == "r":
                my_card.append(f"♥Q")
            elif split_sym == "b":
                my_card.append(f"♠Q")
        elif split_num == 13:
            if split_sym == "m":
                my_card.append(f"♣K")
            elif split_sym == "s":
                my_card.append(f"♦K")
            elif split_sym == "r":
                my_card.append(f"♥K")
            elif split_sym == "b":
                my_card.append(f"♠K")

if my_num[0] == my_num[1] == my_num[2]:
    card_type = "飞机"
else:
    if my_num[0] == my_num[1] != my_num[2] or my_num[0] != my_num[1] == my_num[2] or my_num[0] == my_num[2] != my_num[
        1]:
        card_type = "对子"
    elif my_sym[0] == my_sym[1] == my_sym[2]:
        if my_num[0] - my_num[1] == 1 and my_num[1] - my_num[2] == 1:
            card_type = "顺金"
        elif my_num[0] - my_num[2] == 1 and my_num[2] - my_num[1] == 1:
            card_type = "顺金"
        elif my_num[2] - my_num[1] == 1 and my_num[1] - my_num[0] == 1:
            card_type = "顺金"
        else:
            card_type = "金花"
    else:
        if (my_num[0] + my_num[1] + my_num[2]) / 3 in my_num:
            card_type = "顺子"
        else:
            card_type = "散牌"


print(my_num)
# def compare(card_num, card_type, card_num, card_type2):
#     if card_type == "飞机":
#         if card_type2 == "飞机":



# compare(my_card, card_type, my_card2, card_type2)
# my_card = my_card[0] + my_card[1] + my_card[2]
# print(my_card, card_type)
