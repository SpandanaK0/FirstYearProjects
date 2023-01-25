


from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    tab = [[],[],[],[],[],[],[]]
    stock = Deck()
    stock.shuffle()
    found= [[],[],[],[]]
    waste = []
    for m in range (7):
        for n in range(m,7):
           tab[n].append(stock.deal())

    for val in tab:
        for values in val:
            values.flip_card()
    for val in tab:
        last_card = val[-1]
        last_card.flip_card()
    waste.append(stock.deal())
        
    
    
    return tab,stock,found,waste
    
    
def display(tableau, stock, foundation, waste):

    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" 
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):

    if len(stock)==0:
        return False
    else:
        waste.append(stock.deal())
        return True
    
def check_red(card):
    return card.suit()== 2 or card.suit()== 3 
def check_black(card):
    return card.suit()==1 or card.suit()==4

def waste_to_tableau( waste, tableau, t_num ):

    if len(waste)!= 0:
        if len(tableau[t_num])== 0:
            if waste[-1].rank() == 13:
                tableau[t_num].append(waste.pop())
                return True
            else:
                return False
        elif check_red(tableau[t_num][-1]) and not check_red(waste[-1]):
            if tableau[t_num][-1].rank() - 1 == waste[-1].rank():
                tableau[t_num].append(waste.pop())
                return True 
        elif not check_red(tableau[t_num][-1]) and check_red(waste[-1]):
            if tableau[t_num][-1].rank() - 1 == waste[-1].rank():
                tableau[t_num].append(waste.pop())
                return True 
        
        else:
            return False
    return False


def waste_to_foundation( waste, foundation, f_num ):

    if len(foundation[f_num])== 0 and (waste[-1].rank()== 1):
        foundation[f_num].append(waste.pop())
        return True
    elif len(foundation[f_num])!= 0:
        if foundation[f_num][-1].suit() == waste[-1].suit():
            if foundation[f_num][-1].rank() + 1 == waste[-1].rank():
                foundation[f_num].append(waste.pop())
                return True 
            else:
                return False
        else:
            return False 
    return False 
            

       
        
    

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    

    if len(foundation[f_num])== 0 and (tableau[t_num][-1]).rank()==1:
        foundation[f_num].append(tableau[t_num].pop())
        if len(tableau[t_num]) != 0:
            if (tableau[t_num][-1]).is_face_up() == False:
                tableau[t_num][-1].flip_card()

        return True 
    
    elif len(foundation[f_num])!= 0 :
        if (foundation[f_num][-1].suit()) == (tableau[t_num][-1].suit()):
            if (foundation[f_num][-1].rank()+1)  == (tableau[t_num][-1].rank()):
                foundation[f_num].append(tableau[t_num].pop())
            else:
                return False             
            if len(tableau[t_num]) != 0:
                if (tableau[t_num][-1]).is_face_up() == False:
                    tableau[t_num][-1].flip_card()
            
            return True 
        else: 
            return False 
    else:
        return False 

    






def tableau_to_tableau( tableau, t_num1, t_num2 ):
    if len(tableau[t_num1]) == 0:
        return False
    elif len(tableau[t_num2])== 0 :
        if tableau[t_num1][-1].rank() == 13:
            tableau[t_num2].append(tableau[t_num1].pop())
            if len(tableau[t_num1]) != 0:
                    if (tableau[t_num1][-1]).is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
            return True 
        else:
            return False 
    elif check_red(tableau[t_num1][-1]) and check_black(tableau[t_num2][-1]):
        if (tableau[t_num2][-1].rank()-1)  == (tableau[t_num1][-1].rank()):
            tableau[t_num2].append(tableau[t_num1].pop())
            if len(tableau[t_num1]) != 0:
                    if (tableau[t_num1][-1]).is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
            return True 
        else:
            return False  
    elif check_red(tableau[t_num2][-1]) and check_black(tableau[t_num1][-1]):
        if (tableau[t_num2][-1].rank()-1)  == (tableau[t_num1][-1].rank()):
            tableau[t_num2].append(tableau[t_num1].pop())
            if len(tableau[t_num1]) != 0:
                    if (tableau[t_num1][-1]).is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
            return True 
        else:
            return False 
    else:
        return False 
    

    
def check_win (stock, waste, foundation, tableau):
    if len(stock)== 0 and len(waste) == 0 and len(tableau[0])==0 and len(tableau[1])==0 and len(tableau[2])==0 and len(tableau[3])== 0 and len(tableau[4])== 0 and len(tableau[5])== 0 and len(tableau[6])== 0 and len(foundation[0])==13 and len(foundation[1])==13 and len(foundation[2])==13 and len(foundation[3])==13 :
        return True
    else:
        return False
     
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   


def main(): 
    print(MENU)
    ask_option= ['START']
    tableau,stock,foundation,waste = initialize()    
    display(tableau,stock,foundation,waste)
    
    while ask_option[0] != "Q":
        ask_option = (input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")).upper()
        ask_option = parse_option(ask_option)
        
        if ask_option is None:
            ask_option= ['kk']
            display(tableau,stock,foundation,waste)
            continue
        
        elif ask_option[0] == "TT":
            call_TT= tableau_to_tableau(tableau,(ask_option[1]-1),(ask_option[2]-1))
            if call_TT == False:
                print("\nInvalid move!\n")
                display(tableau,stock,foundation,waste)
                continue
            else:
                checking = check_win(stock, waste, foundation, tableau)
                if checking == True:
                    print("“You won!")
                    display(tableau,stock,foundation,waste)
                    break
                else: 
                    display(tableau,stock,foundation,waste)
        elif ask_option[0] == "TF":
            call_TF = tableau_to_foundation(tableau,foundation,ask_option[1]-1,ask_option[2]-1)
            if call_TF == False:
                print("\nInvalid move!\n")
                display(tableau,stock,foundation,waste)
                continue
            else:
                checking = check_win(stock, waste, foundation, tableau)
                if checking == True:
                    print("“You won!")
                    display(tableau,stock,foundation,waste)
                    continue
                else: 
                    display(tableau,stock,foundation,waste)
        elif ask_option[0]== "WF":
            call_WF = waste_to_foundation(waste,foundation,ask_option[1]-1)
            if call_WF == False:
                print("\nInvalid move!\n")
                display(tableau,stock,foundation,waste)
                continue
            else:
                checking = check_win(stock, waste, foundation, tableau)
                if checking == True:
                    print("“You won!")
                    display(tableau,stock,foundation,waste)
                    break
                else:
                    display(tableau,stock,foundation,waste)
                    continue
        elif ask_option[0]== "WT":
            call_WT = waste_to_tableau(waste,tableau,ask_option[1]-1)
            if call_WT == False:
                print("\nInvalid move!\n")
                display(tableau,stock,foundation,waste)
                continue
            else:
                checking = check_win(stock, waste, foundation, tableau)
                if checking == True:
                    print("“You won!")
                    display(tableau,stock,foundation,waste)
                    break
                else: 
                    display(tableau,stock,foundation,waste)
        elif ask_option[0]== "SW":
            call_SW = stock_to_waste(stock,waste)
            if call_SW == False:
                print("\nInvalid move!\n")
                display(tableau,stock,foundation,waste)
                continue
            else:
                display(tableau,stock,foundation,waste)
        elif ask_option[0] == "R":
            tableau,stock,foundation,waste = initialize()
            display(tableau,stock,foundation,waste)
        elif ask_option[0] == "H":
            print(MENU)
        
        
        

if __name__ == '__main__':
     main()
