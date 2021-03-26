# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:07:01 2021

@author: sonali mali
"""
import random

choice_of_computer = ["Stone","Paper","Scissor"] # computer choice

print("||----You will get 5 Rounds --||")
while True:
    print("Welcome to Rock Paper Scissor Game !!!")
    you_win ,computer_win = 0 ,0
    
    for i in range(1,6):
        print("Round",i, "start !!!")
        print("Please selcet any one option :")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")
        yourchoice=int(input())
         
        if yourchoice == 1:
            print("You select Rock")
            yourchoice="Rock"
        elif yourchoice == 2:
            print("You select Paper")
            yourchoice="Paper"
        elif yourchoice == 3:
            print("You select Scissor")
            yourchoice ="Scissor"
        else:
            print("Invalid Choice")
            break
        
        computer_choice =  random.choice(choice_of_computer)
        print("Computer Select ",computer_choice)
        
        if yourchoice == computer_choice:
            print("This round is drawn you both will not get any points !!!")
            
        elif (yourchoice=="Rock" and computer_choice=="Scissor") or (yourchoice=="Paper" and computer_choice=="Rock") or (yourchoice=="Scissor" and computer_choice=="Paper"):
            you_win +=1
            print("You win this round")
            
        else:
            computer_win +=1
            print("Computer win this round")
    if  you_win >computer_win:
        print("You win the game")
        print("Your score =",you_win ,"Computer Score =",computer_win,sep =" ")
    
    elif you_win<computer_win:
        print("You loose the game. Computer win ths game!!!")
        print("Your score =",you_win ,"Computer Score =",computer_win,sep =" ")
    
    else:
        print("Match Drawn")
        print("Your score =",you_win ,"Computer Score =",computer_win,sep =" ")
    
    user_choice = input("Want to play again ??(Yes/No) :")
    if(user_choice == 'Yes'):
        continue
    else:
        print("Game Ends")
        break
            
        
