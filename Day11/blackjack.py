import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]


#start game

def player_turn(player, sum_player, computer, sum_computer):

    game_over = False
    while not game_over:
        

        if sum_player > 21:
                while 11 in player and sum_player > 21:
                    sum_player-=10
                    player.remove(11)
                    player.append(1)
                print(sum_player)
                if sum_player > 21:
                    print("You lose!")
                    game_over = True
                    break
        elif sum_player == 21:
            print("You win!")
            game_over = True
            break
        
        print(f"You have {player} with score {sum_player}")
        print(f"Computer has {computer} with score {sum_computer}")
        choice = input("Do you want to hit or stand?: ")

        if(choice == "hit"):
            player.append(random.choice(cards))
            sum_player += player[-1]
        elif choice == "stand":
            break

    return game_over

def computer_turn(player, sum_player, computer, sum_computer):

    while(sum_computer < 17 or sum_computer < sum_player):
        computer.append(random.choice(cards))
        sum_computer += computer[-1]

        if sum_computer > 21:
            while 11 in computer:
                sum_computer -= 10
                computer.remove(11)
                computer.append(1)
            if sum_computer > 21:
                print(f"You have {player} with score {sum_player}")
                print(f"Computer has {computer} with score {sum_computer}")
                print("You win!")
                break
        elif sum_computer == 21 or sum_computer > sum_player:
            print(f"You have {player} with score {sum_player}")
            print(f"Computer has {computer} with score {sum_computer}")
            print("You lose!")
            break
        elif sum_computer == sum_player:
            print(f"You have {player} with score {sum_player}")
            print(f"Computer has {computer} with score {sum_computer}")
            print("You draw!")
            break

def Blackjack():

    choice = input("Do you want to play a game of Blackjack? 'Y' or 'N':" )
    while choice == 'Y':
        if choice == 'Y':
            player = [random.choice(cards), random.choice(cards)]
            computer = [random.choice(cards)]

            if not player_turn(player, sum(player), computer, sum(computer)):
                computer_turn(player, sum(player), computer, sum(computer))
        elif choice == 'N':
            print("Goodbye!")
            break
        else: 
            print("Invalid input")
        choice = input("Do you want to play a game of Blackjack? 'Y' or 'N':" )

Blackjack()
        
          


