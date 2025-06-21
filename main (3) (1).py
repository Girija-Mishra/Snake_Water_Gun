'''
1 for snake
-1 for water
0 for gun
'''
import random

user_score=0
computer_score=0
try:
    import winsound
    sound_enabled = True
except:
    sound_enabled = False
while True:
    
    computer=random.choice([-1,0,1])
    your_option = input("Enter your choice (type 's' for Snake 🐍, 'w' for Water 💧, 'g' for Gun 🔫):\n")
    you_Dict={"s":1,"w":-1,"g":0}
    reverse_Dict={1:"Snake 🐍",-1:"Water  💧",0:"Gun 🔫"}
    you=you_Dict[your_option]

    print(f"You chose {reverse_Dict[you]}\nComputer chose {reverse_Dict[computer]}")
 
 
    if(computer==you):
        
       print("It's a draw 🤝")
    else:
        if(computer==-1 and you==1):
           
           print("🎉 You Won!")
           user_score += 1 
           if sound_enabled:
               winsound.Beep(1000, 200)
               
        elif(computer==-1 and you==0):
           print("😞 You Lost")
           computer_score += 1
           if sound_enabled:
               winsound.Beep(400, 200)
               
        elif(computer==1 and you==-1):
           print("🎉 You Won!")
           user_score += 1 
           if sound_enabled:
               winsound.Beep(1000, 200)
               
        elif(computer==1 and you==0):
           print("😞 You Lost")
           computer_score += 1
           if sound_enabled:
               winsound.Beep(400, 200)
               
           
        elif(computer==0 and you==-1):
           print("🎉 You Won")
           user_score += 1
           if sound_enabled:
               winsound.Beep(1000, 200)
           
        elif(computer==0 and you==1):
           print("😞 You Lost")
           computer_score += 1
           if sound_enabled:
               winsound.Beep(1000, 200)
               
           
        else:
           print("❌Smething is invalid")
    play_again=input("\nDo you want to play again?(y/n):").lower()
    if play_again!='y':
        
        print("Thanks for playing! 🎮")
        print(f"\n🏁 Final Showdown Results 🏁\nYou : {user_score}  |  Computer 💻: {computer_score}")
        if user_score > computer_score:
            print("🔥 Victory is Yours! You're the SWG Champion! 🏆")
        elif user_score < computer_score:
            print("💀 Defeated! The Machine Reigns Supreme 🤖")
        else:
             print("⚔️ It's a Tie! A Battle Well Fought 🤝")

        break
    



