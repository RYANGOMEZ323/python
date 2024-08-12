####Tasks:
####
####1. create a list and use random module and apply the below functions:
####choice, choices, random, randrange, randint,sample
####2. use while loop and random module to build a rock paper scissor game and print who won the game!
##
####Tasks:
####
######1. create a list and use random module and apply the below functions:
import random
####from random import *
####l = [1,2,3,4,5,6,7,8,9,10]
####print(choice(l))
####print(choices(l,k=8))
####print(random())
####print(randrange(25))
####print(randint(30,50))
####print(sample(l,k=5))
######2. use while loop and random module to build a rock paper scissor game and print who won the game!
##import random
##user_score = 0
##computer_score = 0
##chance = 0
##options =["rock","paper","scissor"]
##computer = random.choice(options)
##print("welcome to rock , paper , scissor game!!!")
##while chance < 5:
##        user = input("pick any one (rock/paper/scissor):")
##        computer = random.choice(options)
##        print("user : ",user)
##        print("computer : ",computer)
##        if user == computer:
##            print("its a tie! , try again")
##        elif user == "rock" and computer == "scissor":
##            print("you won !")
##            user_score+=1 
##        elif user == "paper" and computer == "rock":
##            print("you won!")
##            user_score+=1
##        elif user == "scissor" and computer == "paper":
##            print("you won !")
##            user_score+=1
##        else:
##            print("computer won !")
##            computer_score+=1
##        print("user score : ",user_score)
##        print("computer score : ",computer_score)
##        if user_score >=3 or computer_score >=3:
##            break
##if user_score >= computer_score:
##    print("congrats!!,you won the game")
##else:
##    print("computer won the game , try again")
##print("Thank you for playing!")
##

##import random
##print("WELCOME TO CHOCOLATE CHOSING GAME!!!")
##chocolates = ["Dairy Milk","KitKat","FiveStar","MilkyBar","Snickers","KinderJoy","Gems"]
##chocolates = random.choice(chocolates)
##attempts = 0
##max_attempts = 100000000
##while attempts < max_attempts :
##        user = input("Enter any chocolates from the below list\n(Dairy Milk,\nKitKat,\nFiveStar,\nMilkyBar,\nSnickers,\nKinderJoy,Gems) : ")
##        if user == chocolates:
##                print("COMPUTER :",chocolates)
##                print("USER :",user)
##                print("YOU HAVE CHOSEN THE CORRECT CHOCOLATE\nYOU WON THE GAME!!!")
##                print("")
##                play_again = input("ENTER 'YES' IF YOU WANT TO PLAY THE GAME AGAIN ELSE 'NO' ")
##                if play_again == "YES":
##                        attempts+=1
##                else:
##                        print("THANK YOU FOR PLAYING THE GAME")
##                        break
##        else :
##                print("COMPUTER :",chocolates)
##                print("USER :",user)
##                print("YOU HAVE CHOSEN THE WRONG CHOCOLATE\nYOU LOSE THE GAME\nTRY AGAIN")
##               
##                attempts+=1
##
##        
##
##                
##

def hello_name(name):
  return ("Hello "+name+"!")
print(hello_name("ryan"))








##
