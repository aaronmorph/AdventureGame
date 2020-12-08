import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def random_speech():
    text = ["There is a funky smell in the air!",
            "I miss home", "Damn, we need to hire a cleaner",
            "I wonder what is happening back on earth",
            "This is gound control to major Tom"]
    print_pause(f'''"{random.choice(text)}""''')


def dice_roll():
    while True:
        print(f"You roll a {random.randint(1,6)}\n")
        break


def tannoy():
    audio = ["HELP, MAYDAY, MAYDAY", "Is anybody out there?!",
             "We have crash landed, please send help",
             "We are under attack"]
    print_pause(f'''"{random.choice(audio)}\n''')


def side_game(items, alien):
    print_pause("Want to roll the dice?")
    while True:
        answer = input("Simply answer, Yes or No\n").lower()
        if answer == "yes":
            dice_roll()
            print_pause('"Wow I am going to have to find some'
                        'other form of entertainment...and fast"\n')
            break
        elif answer == "no":
            print_pause('I do not have time to be messing around\n"')
            main_hall(items, alien)
            break


def quiz_game(items, alien):
    while True:
        answer = input("Please enter your answer >>>\n")
        if answer == "Moscow" or answer == "moscow":
            print_pause("Correct, weapons locker is now open.")
            print_pause("You open the weapons locker and pull"
                        " out a plasma rifle.")
            print_pause('"I am sure this will come in handy"')
            items.append("rifle")
            main_hall(items, alien)
            break
        else:
            print_pause("X X X X\n")
            print_pause("That is incorrect. Please try again Komrade")
            quiz_game(items, alien)


def intro(items, alien):
    n = 10
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("We have ignition and blast off!\n")
    print_pause(r"""

       !
       !
       ^
      / \
     /___\
    |=   =|
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
   /|##!##|\
  / |##!##| \
 /  |##!##|  \
|  / ^ | ^ \  |
| /  ( | )  \ |
|/   ( | )   \|
    ((   ))
   ((  :  ))
   ((  :  ))
    ((   ))
     (( ))
      ( )
       .
       .
       .
""")
    print_pause('"Expidition to Mars is a go."\n')
    print_pause("It's 2030. Two manned rockets set off to Mars..."
                " A long journey is ahead\n")
    print_pause("A year has past and your rocket capsule lands safely on"
                " the already colonized planet Mars.\n")
    print_pause("However there's no sign of the second ship.\n")
    print_pause("You find yourself in the station that the Russian's built"
                " some years earlier.\n")
    print_pause("However there's no sign of life on the station anywhere!\n")
    random_speech()
    print_pause("There are two rooms and one door that appears"
                " to be the exit outside\n")


def main_hall(items, alien):
    print_pause("Where would you like to go?")
    door = input("The armory (door 1)\n"
                 "The locker room (Door 2)\n"
                 "The exit (Door 3)\n"
                 "Please enter 1, 2 or 3\n").lower()
    if door == '1':
        armory(items, alien)
    elif door == '2':
        locker_room(items, alien)
    elif door == '3':
        outside(items, alien)
    else:
        main_hall(items, alien)


def armory(items, alien):
    print_pause("You head over to the door to the left,"
                " the sign reads armory\n")
    if "rifle" in items:
        print_pause('"Looks like there iss nothing left here"\n')
        main_hall(items, alien)
    if "keys" in items:
        print_pause("You use the key you found in the locker room to"
                    " open the door and head inside.")
        print_pause("Once inside you find a locker operated by a computer"
                    " on the screen it reads; 'Kakaya stolitsa Rossii'\n")
        print_pause('"Damn, I knew I should not of skipped Russian'
                    ' lessons!"\n')
        print_pause("Frustrated, you hit the computer!\n")
        print_pause("The screen flickers and turns off but after a"
                    " couple of seconds it comes back on but this time"
                    " with the message 'What is the capital of Russia?'\n")
        quiz_game(items, alien)
    else:
        print_pause("Looks like this door is locked and a key is required\n")
        print_pause('"I wonder if there is a key in the other room"')
        print_pause("You head back out to the main hall\n")
    main_hall(items, alien)


def locker_room(items, alien):
    print_pause("You have to give the door a fair old whack to get in"
                " but once you're in there's nothing much in here\n")
    if "spacesuit" in items:
        print_pause("Looks like I've got everything I need in here so far.")
        print_pause("You hear a rattle in the space suit so you decide"
                    " to rummage around the and find a dirty old die!")
        print_pause('"I wonder if I can still roll my lucky number 4!"')
        side_game(items, alien)
    else:
        print_pause('"Well look what we have here"\n')
        print_pause("You pick up a dirty old space suit and an oxygen tank.")
        print_pause("There is also a key hanging on the back of the door"
                    " which you pick up too.\n")
        print_pause("You head back to the main hallway")
        items.append("keys")
        items.append("spacesuit")
    main_hall(items, alien)


def outside(items, alien):
    print_pause("Just before you head outside, an alarm goes off and"
                " you hear a voice over the tannoy.\n")
    tannoy()
    print_pause('"I need get out there quick!"\n')
    if "spacesuit" in items:
        print_pause("Let's get suited up and booted and get out there!\n")
        print_pause("You get suited up and head towards the crash site\n")
        crashsite(items, alien)
    else:
        print_pause("Are you sure you want to head out there?"
                    " You won't last 1 minute"
                    " without the correct equipment!\n")
        while True:
            answer = input("Please enter yes or no\n")
            if answer == "yes":
                outsidenoequip(items, alien)
                break
            elif answer == "no":
                print_pause("That's the smart thing to do, you head"
                            " back to the hallway")
                main_hall(items, alien)


def crashsite(items, alien):
    print_pause("Just over the horizon you see smoke billowing.")
    print_pause('"That is where the other rocket crash landed!"\n')
    print_pause("You rush over to the fallen craft were stood"
                f" before you is a {alien}\n\n")
    print_pause(f"The {alien} looks at you and just stares deep"
                " into your soul\n")
    print_pause(r'''

       .-""""-.
      /        \
     /_        _\
    // \      / \\
    |\__\    /__/|
     \    ||    /
      \        /
       \  __  /
        '.__.'
''')
    print_pause(f'"I come in peace" you say to the {alien}.'
                ' However it does not')
    if "rifle" in items:
        print_pause("As it goes to attack you, you pull out the"
                    " plasma rile and...\n")
        print_pause("BOOM...\n")
        print_pause(f"The {alien} is dead. You rush to the cockpit of"
                    " the ship and find 2 survivors.")
        print_pause("You carry the 2 crew members back to the station\n")
        print_pause('"Man, Spielberg really got E.T wrong"\n')
        completion()
    else:
        print_pause(f"You're defenseless against the {alien}.\n")
        print_pause("You try and run but it shoots you from behind"
                    " with a plasma rifle.")
        print_pause("Laying there motionless and almost frightned,"
                    "the alien comes up and blasts you from close range.\n")
        print_pause("You die\n")
        death()


def outsidenoequip(items, alien):
    print_pause("You're struggling to breath")
    print_pause("It's not too late to turn back")
    print_pause("do you wish to turn back?")
    answer = input("Please enter yes or no\n").lower()
    if answer == 'yes':
        main_hall(items, alien)
    elif answer == 'no':
        print_pause("You walk a few steps but you can't handle the pressure"
                    " and atmosphere without the correct equipment\n")
        print_pause("You die on surface of the red planet...\n")
        death()
    else:
        outsidenoequip(items, alien)


def death():
    print_pause("Would you like to play again?")
    while True:
        answer = input("Enter yes or no\n")
        if answer == 'yes':
            space_game()
            break
        elif answer == 'no':
            exit_image()
            break
        else:
            death()


def completion():
    answer = input("Congratulations, you have survived the mission to Mars."
                   " Would you like to play again"
                   " or return to earth? Please enter yes to try again"
                   " or no to return to earth\n").lower()
    if answer == 'yes':
        print_pause("Great strap yourself in."
                    "Take off is in T-Minus 10 seconds")
        space_game()
    elif answer == 'no':
        print_pause("Thanks for playing!\n")
        exit_image()
    else:
        completion()


def exit_image():
    print_pause(r'''

    .adOOOOOOOOOba.
   dOOOOOOOOOOOOOOOb
  dOOOOOOOOOOOOOOOOOb
 dOOOOOOOOOOOOOOOOOOOb
|OOOOOOOOOOOOOOOOOOOOO|
OP'~"YOOOOOOOOOOOP"~`YO
OO     `YOOOOOP'     OO
OOb      `OOO'      dOO
YOOo      OOO      oOOP
`OOOo     OOO     oOOO'
 `OOOb._,dOOOb._,dOOO'
  `OOOOOOOOOOOOOOOOO'
   OOOOOOOOOOOOOOOOO
   YOOOOOOOOOOOOOOOP
   `OOOOOOOOOOOOOOO'
    `OOOOOOOOOOOOO'
     `OOOOOOOOOOO'
       `~OOOOO~'   ''')

    print_pause("We are not alone.")
    exit()


def space_game():
    items = []
    alien = random.choice(["Grey Alien", "Green Alien"])
    intro(items, alien)
    main_hall(items, alien)


space_game()
