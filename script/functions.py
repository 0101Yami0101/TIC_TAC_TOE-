# Tic_Tac_Toe
from player import Player
from win import if_game_won




game_Logo = "TIC_TAC_TOE"
dict_template = {
    "sp1": "-",
    "sp2": "-",
    "sp3": "-",
    "sp4": "-",
    "sp5": "-",
    "sp6": "-",
    "sp7": "-",
    "sp8": "-",
    "sp9": "-",
}
##########################################--MAIN GAME FUNCTIONS--###############################################################

# Function to update the spaces
def update_spaces(space_number, symbol:str):
    dict_template[f'sp{space_number}'] = symbol

#Function to check if duplicate entry
def check_duplicate(choice, player_obj):
    if choice in player_obj.spaces_occupied:
        return True
    else:
        return False

# Function to print board
def print_board(updated_dict):  
    '''Function will print updated board with updated spaces'''
    print('\n\n')  
    print(f"  {updated_dict['sp1']} | {updated_dict['sp2']} | {updated_dict['sp3']}  ")
    print("-------------")
    print(f"  {updated_dict['sp4']} | {updated_dict['sp5']} | {updated_dict['sp6']}  ")
    print("-------------")
    print(f"  {updated_dict['sp7']} | {updated_dict['sp8']} | {updated_dict['sp9']}  ")

 #refresh dict
def refresh_template():
    for key in dict_template:
        dict_template[key] = '-'



#main game function
def main_game():
    game_end = False
    player1_symbol = input('Enter your symbol Player1: (X or O) ').upper()
    

    player_list = []

    if player1_symbol == "X":
        
        player1 = Player(symbol="X")
        player2 = Player(symbol="O")
        player_list.append(player1)
        player_list.append(player2)
        
    elif player1_symbol == "O":
        player1 = Player(symbol="O")
        player2 = Player(symbol="X")
        player_list.append(player1)
        player_list.append(player2)
    else:
        print('Invalid Input')
        main_game()



    #Game starts
    print_board(dict_template) 

    #Game loop
    while not game_end:
        for player in player_list: 

            duplicate_spaces_exists = True
            while duplicate_spaces_exists: #'check for duplicates' loop
                player_choice = int(input(f'Enter space number PLAYER {player.symbol} :'))

                for obj in player_list:#check for duplicates in both player objects
                    if check_duplicate(player_choice, obj):
                        print('Duplicate Number ; Enter again')
                        break
                    else:
                        duplicate_spaces_exists = False

            
            #if not duplicate check total spaces first
            total_free_spaces = 8
            for a_player in player_list:
                total_free_spaces -= len(a_player.spaces_occupied) 

            #update spaces 
            if total_free_spaces == 0:
                update_spaces(player_choice, player.symbol) 
                player.spaces_occupied.append(player_choice) 
                print_board(updated_dict= dict_template)

                ##check if player won at the end
                for p in player_list:
                    if if_game_won(p.spaces_occupied):
                        print(f'Congratulations !! Player {player.symbol}.. You win')
                print('GameOver')
                ask = input('Do you wanna play again: y/n').lower()
                if ask == 'n':
                    game_end = True
                    break
                if ask == 'y':
                        refresh_template()

                        main_game()
                
            
                
            else :      
                update_spaces(player_choice, player.symbol)                  
                # print board with new data
                print_board(updated_dict= dict_template)
                # add value to player space list 
                player.spaces_occupied.append(player_choice)

                #check if win
                current_player_combo = player.spaces_occupied 
                if if_game_won(player_combo= current_player_combo):
                    print(f'Congratulations !! Player {player.symbol}.. You win')
                    ask = input('Do you wanna play again:y/n').lower()
                    if ask == 'n':
                        game_end = True
                        break
                    if ask == 'y':
                        refresh_template()

                        main_game()

    

# main_game()

    



































