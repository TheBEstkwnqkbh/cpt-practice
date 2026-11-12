import random

deck = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
deck_values = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand = [ ]
hand_values = [ ]
d_hand = [ ]
d_hand_values = []
table = [ ]
A = [11]
J = [10]
Q = [10]
K = [10]


hand_values.append(random.choice(deck_values))
d_hand_values.append(random.choice(deck_values))
hand_values.append(random.choice(deck_values))


hand.append(random.choice(deck_values))
d_hand.append(random.choice(deck_values))
hand.append(random.choice(deck_values))
print (f"Your hand is {hand}")
print (f"The total of your hand is {sum(hand)}") 
print (f"The dealer's hand is {d_hand}") 

command = input("hit or stand: ")
if command == "hit":
    card = random.choice(deck)
    if card == 'A':
        print("You drew and Ace", A)
        hand_values.append(11)
        hand.append(A)
    elif card == 'J':
        print("You drew a Jack", J)
        hand_values.append(10)
        hand.append(J)
    elif card == 'Q':
        print("You drew a Queen", Q)
        hand_values.append(10)
        hand.append(Q)
    elif card == 'K':
        print("You drew a King", K)
        hand_values.append(10)
        hand.append(K)
    else:
        print("You drew a", card)
        hand_values.append(card)
        hand.append(card)

hand_values.append(random.choice(deck_values))
print (f"Your hand is {hand}")

if command == "stand":
    print("You chose to stand")
    print (f"The total of your hand is {sum(hand)}")
if hand == 21:
    print ("blackjack")
