#hangman_game
#    ++------++
#    |   |
#    |   0 
#    |  /|\
#    | / | \
#    |  / \
#    | /   \
def display_hangman(lives):
    stages = [
        """
           ++------++
           |   |
           |   0
           |  /|\\
           | / | \\
           |  / \\
           | /   \\
        """,
        """
           ++------++
           |   |
           |   0
           |  /|\\
           | / | \\
           |  / 
           | /   
        """,
        """
           ++------++
           |   |
           |   0
           |  /|\\
           | / | \\
           |  
           | 
        """,
        """
           ++------++
           |   |
           |   0
           |  /|\\
           | / | 
           |  
           | 
        """,
        """
           ++------++
           |   |
           |   0
           |  /|\\
           | /  
           |  
           | 
        """,
        """
           ++------++
           |   |
           |   0
           |   |
           |   
           |  
           | 
        """
    ]
    return stages[6 - lives]
    


import random


print("let's paly Hanguman!! game")
n=["custrad","banana","organe","apple","eggplant"]
lives=6
choice=random.choice(n)
lenght=len(choice)
##creat balnk space for a word live
blank=['_']*lenght

game_over = False
while not game_over:
    print(f"lives remaining:{lives}")
    print("current word:"+" ".join(blank))
    guess_letter=input("enter a guess letter: ").lower()
    for position in range(lenght):
        letter = choice[position]
        if letter == guess_letter:
            blank[position] = guess_letter
            #if blank[position] == guess_letter:
                #lives-=1
                
           

    if guess_letter  not in choice:
        lives -= 1
        print(f"{guess_letter} is not in word . try another letter.")
        if lives == 0:
            game_over == True
            print("You Lose the game:",choice)
            break
    if '_' not in blank:
        print("U WIN ! the game:","".join(blank))
        game_over = True
    print(display_hangman(lives))





    
