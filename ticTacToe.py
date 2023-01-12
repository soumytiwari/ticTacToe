import random
from ticTacToeVisuals import TTT_Visuals_dict


"""Conditins to win: 

---(up), ---(down), ---(middle),  <00,01,02/10,11,12/20,21,22>

|       |         |         
|<left>,|<middle>,|<right>,     (00,10,20/01,11,21/02,12,22)
|       |         |    

\       /
 \  ,  /       <00,11,22/02,11,20>
  \   /     
  
  """


def user_choice():
    user_choice=int(input("Enter the position value: "))
    print(f"Your position: {user_choice}")

    return user_choice

def computer_choice():
    computer_choice=random.choice(rest)
    print(f"Computer's choice: {computer_choice}")

    return computer_choice

def win_decision():
    
    horizontal_wins = (horizontal_win1, horizontal_win2, horizontal_win3)
    vertical_wins = (vertical_win1, vertical_win2, vertical_win3)

    for win in horizontal_wins:  
        if set(win).issubset(set(user_choices)):
            print("\n\t-----    You Won!    -----")
            print(TTT_Visuals_dict[0])
            return True

        elif set(win).issubset(set(computer_choices)):
            print("\n\t-----    You Lose...    ")
            print(TTT_Visuals_dict[4])
            return True
    
    for win in vertical_wins:
        if set(win).issubset(set(user_choices)):
            print("\n\t-----    You Won!    -----")
            print(TTT_Visuals_dict[1])
            return True
        elif set(win).issubset(set(computer_choices)):
            print("\n\t-----    You Lose...    ")
            print(TTT_Visuals_dict[5])
            return True

    if set(cross_win1).issubset(set(user_choices)):
        print("\n\t-----    You Won!    -----")
        print(TTT_Visuals_dict[2])
        return True
    elif set(cross_win1).issubset(set(computer_choices)):
        print("\n\t-----    You Lose...    ")
        print(TTT_Visuals_dict[6])
        return True

    if set(cross_win2).issubset(set(user_choices)):
        print("\n\t-----    You Won!    -----")
        print(TTT_Visuals_dict[3])
        return True
    elif set(cross_win2).issubset(set(computer_choices)):
        print("\n\t-----    You Lose...    ")
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

user_choices=[]
computer_choices=[]
rest=[11,12,13,21,22,23,31,32,33]

i=1
while(i<5 and win_decision()!=True):
    user=user_choice()
    user_choices.append(user)
    rest.remove(user)
    win_decision()
    i+=1
    computer=computer_choice()
    computer_choices.append(computer)
    rest.remove(computer)

print("\n\t---    Game Finished.   ---")