import random

def game():
    run = 0
    for x in range(50):
        bowl = random.randint(1,6) 
        bat = int(input("Enter your run(1-6) :"))
        print(f"You : {bat} \ncomputer : {bowl}")
        if(bat != bowl and bat <=6 and bat >= 1):
            run += bat
        else:
            print("Out")
            break
    return run

highscore = 0
i = 1
while(i != 0):
    print("WELCOME TO 50 BALLS HAND CRICKET GAME")
    sum  = game()
    print(sum)
     
    if(highscore >= sum):
        print(f"HighScore : {highscore}")
    else :
        print(f"New HighScore : {sum}")
        highscore = sum
    print("press any key to continue or press 0 to exit")
    i = int(input())