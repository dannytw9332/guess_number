#this game is to guess number
import random

#random number
def rn():
    rn = random.randint(1,100)
    return rn

#main
def main(rn):
    cn = 0
    var1 = 1
    var2 = 100
    while cn != rn:
        print("please enter a number between ",var1, " and ", var2, ":")
        cn = int(input())
        if cn > rn:
            var2 = cn
        elif cn < rn:
            var1 = cn
        else:
            print("you lose!!")

if __name__ == "__main__":
    print("EXPLANATION:")
    print("This game is the guess number. You should enter a number between 1 to 100.")
    print("This range will be stortened when a person guesses a number.")
    print("If players are multiple, please take a turn.")
    print("The person who guesses the number will be a loser.")
    print("\n")
    main(rn())
