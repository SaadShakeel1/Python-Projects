n=15
i = 1
while(i<10):
    print("Enter A Number: ")
    num=int(input())
    if num<n:
        print("Your Guess Is Less Than Number")
    elif num>n:
        print("Your Guess Is Greater Than Number")
    elif num==n:
        print("Your Guess Is Correct")
        print("You Took ",i,"Chance To Guess A Number")
        break
    if i==9:
        print("Game Over The Number Was ",n)
    else:
        print(9-i,"Guesses Left")
    i = i + 1

