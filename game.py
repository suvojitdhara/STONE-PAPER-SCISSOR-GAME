import random
print("Welcome to the STONE PAPER SCISSOR GAME !")
name=input("Enter Your Name : ")
age=int(input("Enter the age : "))
if age>=18:
    while(1):
        C=["stone","paper","scissor"]
        machine=random.choice(C)
        user=input("Enter Choice : ").lower()
        if machine==user:
            print("***Draw***")
        elif machine=='paper':
            if user=='scissor':
                print("***Hey ! ",name,"Congratulations ! You won the Game !***")
            else:
                print("You Loose The GAME")
        elif machine=='stone':
            if user=='paper' :
                print("***Hey ! ",name,"Congratulations ! You won the Game !***")
            else:
                print("You Loose The GAME")
        elif machine=='scissor':
            if user=='stone':
                print("***Hey ! ",name,"Congratulations ! You won the Game !***")
            else:
                print("You Loose The GAME")
        print("Computer chosen : ",machine)
        user1=input("Would you like to play again ! \n")
        if user1=='Yes' or user1=='yes' or user1=='YES' or user1=='y':
            print("Retreving You to the game ...")
        else:
            print("Thank You !")
            break;
else:
    print("You Dont Have The Access !")