print("Welcome to the Circus Circus hotel in Las Vegas!\nWe hope you enjoy your visit.\nHere's your raffle ticket to the summer Circus Circus Lottery!")

location = input("Left or Right?\n")
if location == "Left" or location == "left":
    print("You have chosen to spend your day at the casino!")
    transportation = str(input("Left or Right?\n"))
    if transportation == "Left" or transportation == "left":
        print("\nYou have chosen to ride the creepy, shady elevator down into the confines of the dark and evil casino!\n\n\n(that will steal your soul...)\n")
        print("You press the only button in the elevator...\na large red button with the word DANGER written on it.\nImmediately you feel a sickening sensation as the elevator drops and ascends rapidly!\nAnd finally the elevator comes to a stop at the exact same level you started at.")
        finalchoice = str(input("Left or Right?\n"))
        if finalchoice == "Left" or finalchoice == "left":
            print("\nIn addition to this terrible mess, you see an angry fat security guard giving you the evil eye. Thinking that you ruined the elevator, he then drags you outside the hotel and yells\n'LEAVE NOW!!!'")
            print("GAME OVER")
        else:
            print("\nYou are extremely PISSED at the elevator, but TBH, at the hotel in general! Since you are very angry, you leave Circus Circus in a huff.")
            print("GAME OVER")
    else:
        print("\nYou are a freaking daredevil, especially after eating those brownies, because you chose to jump off the 5th floor down to the dingy casino on level 1.\nUnfortunately, you misjudged your abilities and break your leg on the 3rd floor.")
        print("Feeling dejected, you go to eat at the hotel's diner.\nUnfortunately, you're broke and so security throws you out because you look like a hobo.")
        print("GAME OVER")

#elif childrens section
elif location == "Right" or location == "right":
    print("You have chosen to go to the children's section.")
    transportation2 = str(input("Left or Right?\n"))
    if transportation2 == "Left" or transportation2 == "left":
        print("\nYou have chosen to ride the escalator.\nRight after getting on, your clothing gets caught in the escalator and you topple over all the people in front of you causing a big commotion. Security sees you, and throws you out of the hotel.\n")
        print("GAME OVER")
    else:
        print("\nYou have chosen to take the stairs after hearing all the commotion around the other methods of transportation. After you take your first step, you trip on your shoelace and inelegantly tumble down the staircase.\nYou start crying...")
        crying_solution = str(input("Left or Right?\n"))
        if crying_solution == "Left" or crying_solution == "left":
            print("\nA clown sees you crying and decides to cheer you up by giving you a huge swirly lollipop.\nBeing the spoiled little brat you are, you run towards the expensive statue covered in jewels. Security notices you and grabs you by your arms and dumps you outside.\n")
            print("GAME OVER")
        else:
            #mime
            print("\nHearing you cry, a mime walks up to you and tries to cheer you up with an act. While moving wildly to cheer you up, he accidentally knocks over a one-of-a-kind vase from the Ottoman Empire. Realizing it, he nonchalantly walks away.\nSecurity sees the broken vase next to you looking surprised...\nThey drag you out and toss you into the streets.")
            print("GAME OVER")

#else for neither
else:
    print("Congrats. You're on the worst path possible...\n\nJust Kidding!!! Congratulations! You won a car.\n")
    cont = str(input("Press c to continue!\n"))
    if cont == "c":
        print("You also won a beach house in Malibu, with vacation expenses covered.\nYou have also won the ability to upgrade your phone every time a new version comes out.\nYOU WON THE LOTTERY OF YOUR HOTEL. YOU WIN A MILLION DOLLARS EACH YEAR OF YOU LIFE AND A PRICELESS STATUE WITH DIAMONDS AND OTHER PRECIOUS JEWELS.\n")
    else:
        print("You also won a beach house in Malibu, with vacation expenses covered.\nYou have also won the ability to upgrade your phone every time a new version comes out.\nYOU WON THE LOTTERY OF YOUR HOTEL. YOU WIN A MILLION DOLLARS EACH YEAR OF YOU LIFE AND A PRICELESS STATUE WITH DIAMONDS AND OTHER PRECIOUS JEWELS.\n")
    print("HAVE A GREAT LIFE!:)")
