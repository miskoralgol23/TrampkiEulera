
hands_order = ["HC","OP","TP","Th", "S", "F", "FH", "Fo", "SF", "RF"]


# Loading the data from the source file
with open("p054_poker.txt") as f:
    dat=f.readlines()

dat = [d.replace("\n","") for d in dat]

card_suits = ["C","D","H","S"]
card_numbers = [str(x+2) for x in range(8)]
for num in ["T", "J","Q","K","A"]:
    card_numbers.append(num)

deck =  [num + suit for num in card_numbers for suit in card_suits]


def card_value(cardNo):
    return card_numbers.index(cardNo) + 2

def suit_value(suitLetter):
    return card_suits.index(suitLetter)


def hand_no(n,player=1):
    temp = dat[n][0:14].split() if player==1 else dat[n][15:].split()
    return sorted(temp, key=lambda x: card_value(x[0]) - float(suit_value(x[1]))/4,reverse=True)


from collections import Counter

def cnts(hand):
    n = Counter(map(lambda x: x[0], hand))
    s = Counter(map(lambda x: x[1], hand))
    return (n,s)


if len(x[0]) < 5:
    if len(x[0]) == 4:
        print "Is Pari!!!!!"
    elif len(x[0]) == 3:
        print "Is Threee or Tuper!!!!"
    elif len(x[0]) == 2:
        print "Is four, no nie moge"