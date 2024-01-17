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

def number_guessing_game():


    print("\n\n-------------------------------------")
    print("|        Number Guessing Game       |")
    print("-------------------------------------")

    while True:
        print("\n- - - - - - Main Menu - - - - - -")

        print("\n1 > Start Game")
        print("0 > Exit")

        main_menu_choice = int(input("\nEnter Choice : "))

        if(main_menu_choice == 1):
            
            print("\n-x -x -x -x -x -x -x -x Starting Game -x -x -x -x -x -x -x -x ")
            
            generated_num =  randint(0,100)
            tries = 0
         
            while(True):
                print("\n1 > Guess The Number")
                print("0 > Exit Current Game")

                choice = int(input("\nEnter Choice : "))

                if(choice == 1):
                    print("\nGuess The Number Between 0 TO 100")
                    user_guess_num = int(input("\nEnter Guessed Number : "))
                    tries += 1
                    if(user_guess_num == generated_num):
                        print("\nYou Guessed It Right On ",tries," Tries , Congratulations -x -x -x -x -x -x -x -x")
                        break
                    elif(user_guess_num < generated_num):
                        print("\nBigger Than Guessed Number , " , tries , " Tries . . . . .")
                    else:
                        print("\nSmaller Than Guessed Number , " , tries , " Tries . . . . .")
                elif(choice == 0):
                    print("\nThe Number Is " , generated_num , "\nExited Current Game . . . . . . .")
                    break
                else:
                    print("\nInvalid Input , Please Enter Correct Input Choice")
        elif(main_menu_choice == 0):
            print("\nProgram Exited . . . . . . .")
            break
        else:
            print("\nInvalid Input , Enter Valid Choice Number. . . . . . .")
def main_menu():

    while True:

        print("\n\n----------- Game Main Menu ----------")

        print("\n1 . Rock Paper Scissor")
        print("2 . Number Guessing Game")
        print("0 . Exit")

        main_choice = int(input("\n_ : "))

        if main_choice == 1:

            rock_paper_scissor()

        elif main_choice == 2:

            number_guessing_game()

        elif main_choice == 0:

            print("\n Program Exited , See You Again")
            break

        else:

            print("\nInvalid Input , PLease Check Options And Re Enter Choice")

        
        

