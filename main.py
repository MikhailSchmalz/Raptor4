import time
import random


def print_general(general_message):
    print(general_message)
    time.sleep(1)


def print_warning(warning_message):
    print(warning_message)
    time.sleep(2)

def intro():
    print_general("A warning alarm screams in your ears.")
    print_warning("WARNING: Low Oxygen")
    print_general("Opening your eyes is a chore.")
    print_warning("WARNING: Low Oxygen")
    print_general("With a labored breath you force them open.")
    print_warning("WARNING: Low Oxygen")
    print_general("You scan your console. Only emergency systems"
                  " are online.")
    print_warning("WARNING: Low Oxygen")


def to_die():
    print_general("You have two options: \n"
                  "1. Put on emergency breather.\n"
                  "2. Asphyxiate.")
    response = input("(Please enter 1 or 2)\n")
    if response == '1':
        print_general("You feel relief as your lungs fill with \n"
                      "clean air.")
        print_warning("WARNING: Low Oxygen")
        check_o2()
    elif response == '2':
        print_general("You feel your body slowly drift to nothingness...")
        print_general("You lost...")
        print_general("Would you like to play again?")
        play_again()
    else:
        print_general("Computer can not compute.")
        to_die()

def check_o2():
    oxygen = random.randint(0, 100)
    print_general("You turn off the alarm, and check O2 levels on the breather.")
    print_general("O2 levels are: " + str(oxygen) + "%")
    if oxygen > 50:
        print_general("You have plenty of oxygen to make repairs!")
        repairs()
    elif oxygen > 25:
        print_general("Death is imminent. You must act quickly.")
        repairs()
    elif oxygen < 25:
        print_general("You will die soon.")
        print_general("You feel your body drift to nothingness...")
        print_general("You lost...")
        print_general("Would you like to play again?")
        play_again()

def repairs():
    print_general("You can hear oxygen squealing out of your ship.")
    print_general("You can see a tiny puncture directly above your \n"
                  "head in the glass canopy. But you also notice...")
    time.sleep(3)
    print_general("A candy bar floating just outside the ship! You are hungry.")
    response = input("What do you do?\n"
                     "1. Open the canopy to get the candy bar.\n"
                     "2. Put duct tape on the leak. Sealing it.\n"
                     "(Please enter 1 or 2)\n")
    if response == '1':
        print_general("In order to reach the delicious candy bar you must"
                      " unbuckle.")
        print_general("Your body slowly starts to move toward the bar.")
        print_general("Just as you reach it a piece of debris crashes "
                      "into your ship pushing it away from you rapidly.")
        print_general("As it rushes away your breather is pulled with it!")
        time.sleep(3)
        print_general("You die is seconds.")
        print_general("You lost...")
        print_general("Would you like to play again?")
        play_again()
    elif response == '2':
        print_general("The leaking has stopped!\n"
                      "And you start your ship without faults!")
        print_general("You then fly to safety.")
        print_general("YOU WON!")
        print_general("Would you like to play again?")
        play_again()



def play_again():
    response = input("(Please enter: Y or N)\n").lower()
    if response == 'y':
        raptor4()
    if response == 'n':
        print_general("Thanks for playing!")

def raptor4():
    intro()
    to_die()

raptor4()
