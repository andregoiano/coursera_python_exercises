import random

def name_to_number(name):
    """ Assigns each number to a name """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "You haven't chosen a name!"
        
def number_to_name(number):
    """ Assigns each name to a number """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "You haven't chosen a number!"

def rpsls(player_guess): 
    """ Determines who's the winner, then prints it """
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses", player_guess
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_guess)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_guess = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_guess
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # determine winner, print winner message
    if difference == 1:
        print "Computer wins!"
    elif difference == 2:
        print "Computer wins!"
    elif difference == 3:
        print "Player wins!"
    elif difference == 4:
        print "Player wins!"
    elif difference == 0:
        print "Player and computer tie!" 
    else:
        print "Don't know, this shouldn't be happening!"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")