# Guess-A-Number AI
#
# Marcella Babatunde
# September 1, 2016


import random
import math
import time

def start_screen():
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄      ")     
    print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ")     
    print("▀▀▀▀█░█▀▀▀▀  ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ")     
    print("    ▐░▌      ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌               ")
    print("    ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ")
    print("    ▐░▌      ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ")
    print("    ▐░▌      ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌░▌        ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ")
    print("    ▐░▌      ▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌               ")
    print("    ▐░▌      ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░▌ ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░▌               ")
    print("    ▐░▌      ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌  ▐░▌     ▐░░░░░░░░░░░▌▐░▌               ")
    print("     ▀        ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀    ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀                ")
    print("")                                                                                            
    print(" ▄▄▄▄▄▄▄▄▄▄▄       ▄▄        ▄  ▄         ▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ")
    print("▐░░░░░░░░░░░▌     ▐░░▌      ▐░▌▐░▌       ▐░▌▐░░▌     ▐░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    print("▐░█▀▀▀▀▀▀▀█░▌     ▐░▌░▌     ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌")
    print("▐░▌       ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌")
    print("▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌")
    print("▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    print("▐░█▀▀▀▀▀▀▀█░▌     ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ")
    print("▐░▌       ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  ") 
    print("▐░▌       ▐░▌     ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ")
    print("▐░▌       ▐░▌     ▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌")
    print(" ▀         ▀       ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ ")
    print("************************************************************************************************")
    print("*                                                                                              *")
    print("*                                  Press Enter to Play                                         *")
    print("*                                                                                              *")
    print("************************************************************************************************")

    input()


def credit():

    print("")
    print("")
    print("")
    print("")
    print("")
    print("***************************************************************")
    print("*                Made by: Marcella Babatunde                  *")
    print("*                        On: 9/7/16                           *")
    print("***************************************************************")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    time.sleep(.05)
    print("")
    
def play():

    tries = 0
    num = random.randint
    low = 1
    high = 100
    limit = int(math.log(high - low, 2)) + 1
    tries = 0
    print("Think of a number from " + str(low) + " to " + str(high) + ".")
    print("I will try to guess it.")
    print("Press ENTER to continue")

    input()

    got_it = False
    while got_it == False:
        tries = tries + 1
        guess = (high + low) // 2
        print("Is your number " + str(guess) + "?")
        print("If no type 'higher' or 'lower'")
        response = input()
        response = response.lower()

        if response == "lower" or response == "l":
            high = guess - 1

        elif response == "higher" or response == "h":
            low = guess + 1

        elif response == "yes" or response == "y":
            got_it = True
        
    if got_it == True:
        print("I win")
        print("I guessed the number in " + str(tries) + ".")
def play_again():
    while True:
        answer = input("Would you like to play agian?")
        answer = answer.lower()

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes' or answer == 'y':
            return True

print("Answer yes or no")

start_screen()

again = True
while again == True:
    play()
    again = play_again()



print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
print(" ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
print(" ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
print(" ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
print(" ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
print("  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
credit()                   


                                                                                                
