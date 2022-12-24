import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
sci = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")



game_images = [rock, paper, sci]


user_choice = int(input(f"Enter Your Choice : 0 for rock, 1 for paper, 2 for scissors : "))

computer_choice = random.randint(0,2)
print(computer_choice, user_choice)

print(game_images[computer_choice])
print(game_images[user_choice])

''''if user_choice == 0 and computer_choice == 0:
    print("Its A Draw")
elif user_choice == 1 and computer_choice == 1:
    print("It's A Draw")
elif user_choice == 2 and computer_choice == 2:
    print("It's A Draw")'''
    
if computer_choice == user_choice:
    print("It's A Draw")

#User choice Rock
elif user_choice == 0 and computer_choice == 1:
    print("You Won")
elif user_choice == 0 and computer_choice == 2:
    print("Computer won")

#User Choice Paper
elif user_choice == 1 and computer_choice == 0:
    print("You won")
elif user_choice == 1 and computer_choice == 2:
    print("computer won")
    
#User Choice Scissors   
elif user_choice == 2 and computer_choice == 1:
    print("Computer won")
elif user_choice == 2 and computer_choice == 0:
    print("computer won")
    
else:
    print("Please Enter Vaid Choice")
