from random import randint

def rock_paper_scissor():

    def getChoiceName(choice: int) -> str:
        if choice == 1:
            return "Rock"
        elif choice == 2:
            return "Paper"
        elif choice == 3:
            return "Scissor"
        else:
            return "Invalid"

    print("\n\n-------------------------------------")
    print("|         Rock Paper Scissor        |")
    print("-------------------------------------")


    while True:

        print("\n------------ Rock Paper Scissor Main Menu -------------")
        print("\n1 Rock\n2 Paper\n3 Scissor")

        user_input = int(input("\n_ : "))
        computer_response = randint(1,3)

        print("\nYour Choice = " + getChoiceName(user_input))
        print("Computer Choice = " + getChoiceName(computer_response))

        if user_input < 1 or user_input > 3:
            print("\nInvalid Input")
        elif user_input == 2 and computer_response == 1:
            print("\nComputer Wins")
        elif user_input == 2 and computer_response == 3:
            print("\nComputer Wins")
        elif user_input == 3 and computer_response == 1:
            print("\nComputer Wins")
        elif user_input == computer_response:
            print("\nTie")
        else:
            print("\nYou Win")

        
        another_game = input("\nLet's Try Another Time (y/n) : ")

        if another_game.lower() == "y":
            continue
        else:
            print("\nPlay Another Time, See You Soon")
            break


def main_menu():

    while True:

        print("\n\n----------- Game Main Menu ----------")

        print("\n1 . Rock Paper Scissor")
        print("0 . Exit")

        main_choice = int(input("\n_ : "))

        if main_choice == 1:

            rock_paper_scissor()

        elif main_choice == 0:

            print("\n Program Exited , See You Again")
            break

        else:

            print("\nInvalid Input , PLease Check Options And Re Enter Choice")

        
        

