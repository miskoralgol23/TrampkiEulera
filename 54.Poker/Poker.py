import pdb
hands_order = ["HC","OP","TP","Th", "S", "F", "FH", "Fo", "SF", "RF"]


# Loading the data from the source file
#############################################
with open("p054_poker.txt") as f:
    dat=f.readlines()

dat = [d.replace("\n","") for d in dat]

card_suits = ["C","D","H","S"]
card_numbers = [str(x+2) for x in range(8)]
for num in ["T", "J","Q","K","A"]:
    card_numbers.append(num)

deck =  [num + suit for num in card_numbers for suit in card_suits]
#############################################

def card_value(cardNo):
    return card_numbers.index(cardNo) + 2


def suit_value(suitLetter):
    return card_suits.index(suitLetter)


def hand_no(n,player=1):
    """returns the 5 cards for player one if the second parameter is not given or is equal to 1, otherwise returns the
    5 cards belonging to player 2"""
    return dat[n][0:14].split() if player==1 else dat[n][15:].split()

from collections import Counter

def cnts(hand):
    n = Counter(map(lambda x: x[0], hand))
    s = Counter(map(lambda x: x[1], hand))
    return (n,s)


def isStraight(cards):
    cards=[card_value(x[0]) for x in cards]
    cards=sorted(cards)
    cards=[c - cards[0] for c in cards]
    if cards==[0,1,2,3,4]:
        return(True)

def hand_conf(cards):
    interim_result="HC"
    x=cnts(cards)
    if len(x[1])==1:
        interim_result="F"
    imm=filter(lambda y:y>1,x[0].values())
    multiple=sorted(list(imm),reverse=True)
    if len(multiple)>0:
        if multiple==[2]:
            interim_result="OP"
        if multiple==[3,2]:
            interim_result="FH"
        if multiple==[3]:
            interim_result="Th"
        if multiple==[4]:
            interim_result="Fo"
        if multiple==[2,2]:
            interim_result="TP"
    else:
        if isStraight(cards):
            if interim_result=="F":
                interim_result="SF"
            else:
                interim_result="S"
    return hands_order.index(interim_result)

def hand_val(cards):
    num_cnt=cnts(cards)[0]
    cards=[(card_value(x[0])*15)**(num_cnt[x[0]]+1) for x in cards]
    return(cards)

def run_some_test():
    for x in range(4):
        tst=hand_no(x)
        tzt=hand_no(x,2)
        conf=hand_conf(tst)
        conf2=hand_conf(tzt)
        print(str(tst) + "  "+ str(x) + " "+ str(conf) + " Val " + str(hand_val(tst)) +"="+ str(sum(hand_val(tst))))
        print(str(tzt) + "  "+ str(x) + " "+ str(conf2) + " Val " + str(hand_val(tzt)) + "=" + str(sum(hand_val(tzt))))

run_some_test()
