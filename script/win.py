#Victory checking and scores counter

list_of_conditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]



def if_game_won(player_combo):
    '''Takes in player's space_occupied list and checks if it matches any win combination'''
    
    # check if len is atleast 3
     #optimization
    if (len(player_combo) < 3):
        return False
    else:
        for combo in list_of_conditions: #[1,2,3]  
            pass_counter = 0
            for num in combo: #1 /// check for first element in the player combo
                
                if num in player_combo:
                    pass_counter += 1
                else:
                    break  #change to new combo if the num is not present

                #if this pass 3 times- condition is successful
                if pass_counter == 3:
                    return True
                    
                
            
                
                
 
      


