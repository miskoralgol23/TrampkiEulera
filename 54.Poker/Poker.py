"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

HC - High Card
OP - One Pair
TP - Two Pairs
Th - Three of a Kind
S - Straight
F - Flush
FH - Full House
Fo - Four of a Kind
SF - Straight Flush
RF - Royal Flush
"""

c_dict = {"J":"Jack","Q":"Queen","K":"King","A":"Ace"}
hands_order = ["HC","OP","TP","Th", "S", "F", "FH", "Fo", "SF", "RF"]

with open("p054_poker.txt") as f:
    dat=f.readlines()

dat = [d.replace("\n","") for d in dat]

def game_no(n):
    return dat[n]

card_suits = ["C","D","H","S"]
card_numbers = [str(x+2) for x in range(8)]

def card_value(cardNo):
    return card_numbers.index(cardNo) + 2

def suit_value(suitLetter):
    return card_suits.index(suitLetter)

def hand_no(n,player=1):
    temp = game_no(n)[0:14].split() if player==1 else game_no(n)[15:].split()
    return sorted(temp, key=lambda x: card_value(x[0]) - float(suit_value(x[1]))/4,reverse=True)

for num in ["T", "J","Q","K","A"]:
    card_numbers.append(num)

deck =  [num + suit for num in card_numbers for suit in card_suits]

from collections import Counter

def cnts(hand):
    n = Counter(map(lambda x: x[0], hand))
    s = Counter(map(lambda x: x[1], hand))
    return (n,s)

h = hand_no(9)
print(h)
x = cnts(h)

if len(x[0]) < 5:
    if len(x[0]) == 4:
        print "Is Pari!!!!!"
    elif len(x[0]) == 3:
        print "Is Threee or Tuper!!!!"
    elif len(x[0]) == 2:
        print "Is four, no nie moge"