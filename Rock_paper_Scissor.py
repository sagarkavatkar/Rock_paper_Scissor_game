import random

rock='''
    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor='''
       _ _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Enter your choice for rock enter 0\n for paper enter 1\n for scissor enter 2")
Your_choice=int(input())
if Your_choice==0:
    Your_choice=rock
elif Your_choice==1:
    Your_choice=paper
elif(Your_choice==2):
    Your_choice=scissor
else:
    print("Enter a valid No.")
computer=random.randint(1,3)
if(computer==1):
    computer=rock
elif(computer==2):
    computer=paper
else:
    computer=scissor
if(Your_choice==rock and computer==rock):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("The Match is Draw")
if(Your_choice==rock and computer==paper):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("Computer won the match")
if(Your_choice==rock and computer==scissor):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("You won the match")
if(Your_choice==paper and computer==rock):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("you won the match")
if(Your_choice==paper and computer==paper):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("draw match")
if(Your_choice==paper and computer==scissor):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("Computer won the match")
if(Your_choice==scissor and computer==rock):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("computer won the match")
if(Your_choice==scissor and computer==paper):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("you won the match")
if(Your_choice==scissor and computer==scissor):
    print("Your Entered Choice")
    print(Your_choice)
    print("Computer Choice")
    print(computer)
    print("draw the match")

 