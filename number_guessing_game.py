import random
play = "yes"
while play == "yes":

    number = random.randint(1,100)

    attempt=0
    guess= int(input("guess the number:"))
    attempt = attempt+1

    while guess !=number and attempt<10:
        if guess > number:
         print("to high!")
        else:
            print("to low!")

        guess = int(input("guees agian:"))
        attempt=attempt+1

    if guess == number:
     print("correct")
     print("attempt",attempt)
    else:
        print("game over")
        print("the number was:",number) 

    play = input("Do you want to play again? (yes/no): ")