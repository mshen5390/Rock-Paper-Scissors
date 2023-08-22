import random

user = input("Username: ")      # gives user the ability to create a username that will later be used as an identifier
password = input("Password: ")      # a unique password that will allow only people who know the password to be allowed to access

check_password = input("Re-Enter Password for verification: ")
while check_password != password:
    check_password = input("Re-Enter Password for verification: ")
# checks the password so that user didn't accidentally type the wrong password

def compResult():
    rps = ["Rock", "Paper", "Scissors"]
    return rps[random.randrange(3)]
# determines the computer result

def game():
    # main function for game
    comp = compResult()
    user_in = str(input("Rock, Paper, or Scissors? ").capitalize())

    # gets input from user

    if comp == user_in:
        print("Computer: " + comp + "\n" + user + ": " + user_in + "\n It's a Tie")
    elif comp == "Rock" and user_in == "Scissors" or comp == "Scissors" and user_in == "Paper" or comp == "Paper" and user_in == "Rock":
        print("Computer: " + comp + "\n" + user + ": " + user_in + "\n" + user + " has Lost!")
    elif comp == "Rock" and user_in == "Paper" or comp == "Scissors" and user_in == "Rock" or comp == "Paper" and user_in == "Scissors":
        print("Computer: " + comp + "\n" + user + ": " + user_in + "\n" + user + " has Won!")
    else:
        print("Please Spell Correctly\n")

    # compares input to computer results to determine winner

game() # calls game function


def play_again():
    return input("Do you want to play again? Yes/No ").capitalize()

def again():
    playing = True
    while playing:
        if play_again() == "Yes":
            game()
        else:
            playing = False
again()

# functio to determines if user wants to play again

