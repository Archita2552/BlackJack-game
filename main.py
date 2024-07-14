from art import logo
print(logo)
import random

def calculateSum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(sum_user, sum_computer):
    if sum_user == sum_computer:
        print("It's a draw")
    elif sum_computer == 0:
        print("Computer wins")
    elif sum_user == 0:
        print("You win")    
    elif sum_computer > 21:
        print("You win")
    elif sum_user > 21:
        print("Computer wins") 
    elif sum_computer > sum_user:
        print("Computer wins")       
    else:
        print("You win") 

user_cards = []
computer_cards = []
is_game_over = False

def dealcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

for num in range(0, 2):
    user_cards.append(dealcard())
    computer_cards.append(dealcard())

while not is_game_over:    
    sum_user = calculateSum(user_cards)    
    sum_computer = calculateSum(computer_cards)
    print(f"Your Cards: {user_cards}, and your current score: {sum_user}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if sum_user == 0 or sum_computer == 0 or sum_user > 21:
        is_game_over = True
    else:
        choice = input("Do you want to hit? Press 'y' or stand? Press 'n': ")
        if choice == 'y':
            user_cards.append(dealcard())
        else:
            is_game_over = True    

while sum_computer != 0 and sum_computer < 17:
    computer_cards.append(dealcard())
    sum_computer = calculateSum(computer_cards)

print(f"Your final hand: {user_cards}, and your final score: {sum_user}")   
print(f"Computer's final hand: {computer_cards}, and computer's final score: {sum_computer}")        
compare(sum_user, sum_computer)
