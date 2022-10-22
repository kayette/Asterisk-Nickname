import time
import sys

def greetUser():
    hello = ("\n\u001b[35mHello user, welcome to " + '\033[3m' + '\033[1;33mWRITTEN IN THE STARS' + '\033[0m' + "\n\u001b[35mThis program lets you write your name in the universe as stars! Try it with me!")
    for i in hello:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03),
    print()
    loadingScreen = "...\n...\n...\n \n"
    for i in loadingScreen:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2),
    print()

def starname():
    starK = [[" " for i in range(5)] for j in range(7)]
    starA = [[" " for i in range(5)] for j in range(7)]
    starY = [[" " for i in range(5)] for j in range(7)]
    color = "\033[1;33m"

    A=0
    B=4
    for row in range(7):
        for col in range(5):
            if col==0 or (row==col+2 and col>1):
                starK[row][col] = "*"
            elif ((row==A and col==B) and col>0):
                starK[row][col] = "*"
                A=A+1
                B=B-1

    for row in range(7):
        for col in range(5):
            if (col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)):
                starA[row][col] = "*"

    for row in range(7):
        for col in range(5):
            if (col==2 and row>1) or (row==col and col<2) or (row==0 and col==4) or (row==1 and col==3):
                starY[row][col] = "*"

    for i in range(7):
        for j in range(5):
            print(color, starK[i][j], end=" ")
        print(end="  ")
        for j in range(5):
            print(color, starA[i][j],end=" ")
        print(end="  ")
        for j in range(5):
            print(color, starY[i][j], end=" ")
        print(end="  ")
        print()

def exit():
    outro = "\n\u001b[35mThank you for viewing " + '\033[3m' + '\033[1;33mWRITTEN IN THE STARS' + '\033[0m' + "\n\u001b[35mThe universe is glad to have you.\n"
    for i in outro:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06),
    print()

greetUser()
starname()
exit()