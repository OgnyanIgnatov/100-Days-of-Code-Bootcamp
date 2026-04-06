import random, game_data

data = game_data.data


def Higher_Lower_Game():
    print("Welcome to the Higher or Lower game!")

    comparent_one = random.choice(data)
    comparent_two = random.choice(data)
    counter = 0

    while True: 
        print(f"Compare A: {comparent_one['name']}, a {comparent_one['description']}, from {comparent_one['country']}")
        print("""
              VS
              """)
        print(f"Compare B: {comparent_two['name']}, a {comparent_two['description']}, from {comparent_two['country']}")
        answer = input("Who has more followers? \"A\" or \"B\"?: ")

        if answer == 'A':
            if comparent_one['follower_count'] < comparent_two['follower_count']:
                print(f"You lose! Your score is {counter}")
                break
        elif answer == 'B':
            if comparent_one['follower_count'] > comparent_two['follower_count']:
                print(f"You lose! Your score is {counter}")
                break
        else: 
            print("Invalid input! Please try again!")
            continue
        
        counter += 1
        print(f"""
              You guessed correctly! Your score now is {counter}
            """)
        comparent_one = comparent_two
        comparent_two = random.choice(data)

Higher_Lower_Game()


    