import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



def game():
    images = [rock, paper, scissors]
    
    choice1 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    choice2 = random.randint(0, 2)
    choice1 = int(choice1)
    
    print(images[choice1])
    print("Computer chose:")
    print(images[choice2])
    
    if choice1 >= 3 or choice1 < 0:
        print("You typed an invalid number, You lose!")   
        
    elif choice1 == 0 and choice2 == 2:
        print("You wins.")
        
    elif choice2 == 0 and choice1 == 2:
        print("You lose.")
        
    elif choice1 < choice2:
        print("You lose.")
        
    elif choice1 == choice2:
        print("It's a draw.")
    
    choice = input("Do you want to play another round? Type 'y' or 'n': ")
    if choice == 'y':
        game()

game()