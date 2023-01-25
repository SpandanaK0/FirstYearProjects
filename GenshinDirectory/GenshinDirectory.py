
import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    file_input = input("Enter file name: ")
    while True:
        try:
            open_file = open(file_input)
            return open_file
        except FileNotFoundError:
            #if it can't find the file will return error msg and ask question again 
            print("\nError opening file. Please try again.")
            file_input = input("Enter file name: ")


def read_file(fp):
    reading = csv.reader(fp)
    next(reading,None)
    data =[]
    for line in reading:
        name = line[0]
        element = line[2]
        weapon = line[3]
        rarity = int(line[1])
        region = line[4]
        if region == '':
            region =None
        tup = (name,element, weapon, rarity, region)
        data.append(tup)

    return (data)
def get_characters_by_criterion (list_of_tuples, criteria, value):
    output_list =[]
    for check in list_of_tuples:
        if criteria== RARITY:
            if check[criteria]== value:
                output_list.append(check)
        else:
            if check[criteria] and check[criteria].lower() == value.lower() and value == str(value):
                output_list.append(check)
    return output_list
    
    
        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    get_list = get_characters_by_criterion(master_list,WEAPON,weapon)
    get_list = get_characters_by_criterion(get_list,RARITY,rarity)
    get_list= get_characters_by_criterion(get_list,ELEMENT,element)
    return get_list
    

def get_region_list  (master_list):
    region_tup = []
    for var in master_list:
        region = var[4]
        if region != None:
            if region in region_tup:
                continue
            else:
                region_tup.append(region)
    
    return sorted(region_tup)



def sort_characters (list_of_tuples):
    
    sor = sorted(list_of_tuples, key=itemgetter(3), reverse=True)
    return sor


def display_characters (list_of_tuples):

    if list_of_tuples == []:
        print ("\nNothing to print.")
    else:
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity", "Region" ))
    for i in list_of_tuples:
        name = i[0]
        element = i[1]
        weapon = i[2]
        rarity = i[3]
        region = i[4]
        if region == None:
            region = "N/A"
        print(ROW_FORMAT.format(name,element,weapon,int(rarity),region))

    

         
def get_option():
    while True:
        input_menu = input(MENU)
        try:
            change = int(input_menu)
            if 0<change<= 4:
                return change
            else:
                print("\nNothing to print.")
        except ValueError:
            print("\nNothing to print.")

  
def main():
    openFile = open_file()
    openRead = read_file(openFile)
    getOption= (get_option())
    while getOption != 4:
        if getOption == 1 :
            print("\nRegions:")
            x = ", ".join(get_region_list(openRead))
            print(x)
        elif getOption == 2:
            ask_cri = input(CRITERIA_INPUT)
            try:
                change_cri_int = int(ask_cri)
            except ValueError:
                print(INVALID_INPUT)
                ask_cri = input(CRITERIA_INPUT)
            
            ask_val = input(VALUE_INPUT)
            if change_cri_int == RARITY:
                try:
                    int_change_val = int(ask_val)
                    get_crit = get_characters_by_criterion(openRead,change_cri_int,int_change_val)
                except ValueError:
                    print(INVALID_INPUT)
                    ask_val = input(VALUE_INPUT)
            else:        
                get_crit = get_characters_by_criterion(openRead,change_cri_int,ask_val)
            sort_ch = sort_characters(get_crit)
            dis = display_characters(sort_ch)
                                


                    
        
        
        elif getOption == 3:
            ask_element = input(ELEMENT_INPUT)
            ask_weapon = input(WEAPON_INPUT)
            ask_rarity = input (RARITY_INPUT)
            try:
                chang_rar = int(ask_rarity)
            except ValueError:
                print(INVALID_INPUT)
                ask_rarity = input(RARITY_INPUT)
            cal_fun_crit = get_characters_by_criteria(openRead,ask_element,ask_weapon,chang_rar)
            sort_cri = sort_characters(cal_fun_crit)
            display_cri = display_characters(sort_cri)
        

        getOption= get_option()
    

if __name__ == "__main__":
    main()
    
