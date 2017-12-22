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

c_dict = {
"J":"Jack",
"Q":"Queen",
"K":"King",
"A":"Ace"}


with open("p054_poker.txt") as f:
    dat=f.readlines()

dat = [d.replace("\n","") for d in dat]

hands_order = ["HC","OP","TP","Th", "S", "F", "FH", "Fo", "SF", "RF"]

def game_no(n):
    return dat[n]


"""
Wszystko ladnie pieknie poki co, ale co jezeli bedziemy mieli skrypt odplaony np z katalogu ppnizej tak ze nie ma czegos takiego pliku jak "poker'txt" w biezacym katalogu"""


def hand_no(n,player=1):
    return game_no(n)[0:14] if player==1 else game_no(n)[15:]

card_suits = ["D","H","C","S"]
card_numbers = [str(x+2) for x in range(9)]
card_numbers.append("J")
card_numbers.append("Q")
card_numbers.append("K")
card_numbers.append("A")

deck =  [num + suit for num in card_numbers for suit in card_suits]



