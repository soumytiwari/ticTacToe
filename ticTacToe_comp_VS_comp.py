import random
from ticTacToeVisuals import TTT_Visuals_dict

def computer_choice():
    computer_choice=random.choice(rest)
    print(f"Computer's choice: {computer_choice}")

    return computer_choice

def win_decision():
    
    horizontal_wins = (horizontal_win1, horizontal_win2, horizontal_win3)
    vertical_wins = (vertical_win1, vertical_win2, vertical_win3)

    for win in horizontal_wins:  
        if set(win).issubset(set(player1_choices)):
            print("\n\t-----    Player1 Won!    -----")
            print(TTT_Visuals_dict[0])
            return True

        elif set(win).issubset(set(player2_choices)):
            print("\n\t-----        Player2 Won!    -----")
            print(TTT_Visuals_dict[4])
            return True
    
    for win in vertical_wins:
        if set(win).issubset(set(player1_choices)):
            print("\n\t-----        Player1 Won!    -----")
            print(TTT_Visuals_dict[1])
            return True
        elif set(win).issubset(set(player2_choices)):
            print("\n\t-----        Player2 Won!    -----")
            print(TTT_Visuals_dict[5])
            return True

    if set(cross_win1).issubset(set(player1_choices)):
        print("\n\t-----        Player1 Won!    -----")
        print(TTT_Visuals_dict[2])
        return True
    elif set(cross_win1).issubset(set(player2_choices)):
        print("\n\t-----        Player2 Won!    -----")
        print(TTT_Visuals_dict[6])
        return True

    if set(cross_win2).issubset(set(player1_choices)):
        print("\n\t-----        Player1 Won!    -----")
        print(TTT_Visuals_dict[3])
        return True
    elif set(cross_win2).issubset(set(player2_choices)):
        print("\n\t-----        Player2 Won!    -----")
        print(TTT_Visuals_dict[7])
        return True

    return print("\n\t-----    Match Draw")


#for now user is only having '0'
#let's take user input as not 1,1 but 11


horizontal_win1=[11,12,13]
horizontal_win2=[21,22,23]
horizontal_win3=[31,32,33]

vertical_win1=[11,21,31]
vertical_win2=[12,22,32]
vertical_win3=[13,23,33]

cross_win1=[11,22,33]
cross_win2=[13,22,31]

player1_choices=[]
player2_choices=[]
rest=[11,12,13,21,22,23,31,32,33]

i=1
while(i<5 and win_decision()!=True):
    player1=computer_choice()
    player1_choices.append(player1)
    rest.remove(player1)
    win_decision()
    i+=1
    player2=computer_choice()
    player2_choices.append(player2)
    rest.remove(player2)

print("\n\t---    Game Finished.   ---")