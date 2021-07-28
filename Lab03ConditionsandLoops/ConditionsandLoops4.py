import random

comp_points = 0
player_points = 0


def choose_option():
    user_choice = input("Rock, Paper or Scissors: ")
    if user_choice in ["Rock","rock"]:
        user_choice = "Rock"
    elif user_choice in ["Paper","paper"]:
        user_choice = "Paper"
    elif user_choice in ["Scissors", "scissors"]:
        user_choice = "Scissors"
    else:
        print("Invalid choice, try again.")
        choose_option()
    return user_choice


def computer_option():
    comp_guess = random.randint(0,2)
    if comp_guess == 0:
        comp_guess = "Rock"
    elif comp_guess == 1:
        comp_guess == "Paper"
    else:
            comp_guess == "Scissors"
    return comp_guess

while True:
    print("")

    user_choice = choose_option()
    comp_guess = computer_option()

    print("")

    if user_choice == "Rock":
        if comp_guess == "Rock":
            print("We have a tie!")

        elif comp_guess == "Paper":
            print("User chose Rock. Computer chose Paper. You lose!")
            comp_points += 1

        elif comp_guess == "Scissors":
            print("User chose Rock. Computer chose Scissors. You win!")
            player_points += 1
    
    elif user_choice == "Paper":
        if comp_guess == "Rock":
            print("User chose paper. Computer chose Rock. You win")
            player_points += 1

        elif comp_guess == "Paper":
            print("We have a tie!")

        elif comp_guess == "Scissors":
            print("User chose paper. Computer chose scissors.You lose!")
            comp_points += 1

    elif user_choice == "Scissors":
        if comp_guess == "Rock":
            print("User chose Scissors. Computer chose Rock. You lose!")
            comp_points += 1

        elif comp_guess == "Paper":
            print("User chose Scissors. Computer chose Paper. you win!")
            player_points += 1

        elif comp_guess == "Scissors":
            print("We have a tie!")

    print("")
    print("Player points: " + str(player_points))
    print("Computer points: " + str(comp_points))
    print("")

    user_choice = input ("Do you want to play again? (y/n)")
    if user_choice in ["y"]:
        pass
    elif user_choice in ["n"]:
        break
    else:
        break






 

