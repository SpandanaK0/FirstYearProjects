
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
def open_file(s):
    ask_file = input(("\nInput a {} file: ").format(s))
    s.lower()
    while True:
        try:
            fp = open(ask_file,"r")
            return fp
        except FileNotFoundError:
            print("\nError in opening file.")
            ask_file = input("\nInput a {} file: ").format(s)


def read_names(fp):
    list_of_names = []
    for line in fp:
        line_strip = line.strip()
        list_of_names.append(line_strip)
    return list_of_names

def read_friends(fp,names_lst):
    friends_of_list = []
    total_friends = []
    for line in fp:
        line_str = line.strip().split(",") 

        for i in line_str:
            if i != "":
                val= int(i)
                total_friends.append(names_lst[val])

        friends_of_list.append(total_friends)
        total_friends = []

    return friends_of_list


def create_friends_dict(names_lst,friends_lst):
    d= dict(zip(names_lst,friends_lst))    
    return d

def find_common_friends(name1, name2, friends_dict):

    name1_sec = friends_dict[name1]
    name2_sec = friends_dict[name2]
    name1_set = set(name1_sec)
    name2_set = set(name2_sec)
    var = (name1_set).intersection(name2_set)
    return var


def find_max_friends(names_lst, friends_lst):

    end_fri = []
    end_name = []
    for i in friends_lst:
        max_fri = len(i)
        end_fri.append(max_fri)
    fri_max = max(end_fri)
    for n, line in enumerate(names_lst):
        if end_fri[n]== fri_max:
            end_name.append(line)
    name_sort = sorted(end_name)
    return name_sort, fri_max
    
    return max_fri


def find_max_common_friends(friends_dict):

    f_dict= {}  
    end_value =[]
    for i in friends_dict:
        for n in friends_dict:
            if i == n:
                continue
            if (n,i) in f_dict:
                continue
            if n in friends_dict[i] or i in friends_dict[n]:
                continue
            find_com = find_common_friends(i,n,friends_dict)
            tup = (i,n)
            common_friends = len(find_com)
            f_dict[tup]= common_friends
    max_var = max(f_dict.values()) 
    for v in f_dict:
        if f_dict[v]== max_var:
            end_value.append(v)
    end_value.sort()
    return end_value, max_var

def find_second_friends(friends_dict):

    second_f_dict = {}
    for friend1 in friends_dict.keys():
        friend1_set = set()
        for friend2 in friends_dict[friend1]:
            for i in friends_dict[friend2]:
                friend1_set.add(i)
        friend1_set= friend1_set- set(friends_dict[friend1]) - {friend1}
        second_f_dict[friend1]= friend1_set
    return second_f_dict 

            


def find_max_second_friends(seconds_dict):
    sec_max_friends= []
    secMax_name = []
   
    for i in seconds_dict.values():

        maxSec_fri = len(i)
        sec_max_friends.append(maxSec_fri)
    friSec_max = max(sec_max_friends)
    
    for m, line in enumerate(seconds_dict):
        if sec_max_friends[m]== friSec_max:
            secMax_name.append(line)
    secName_sort = sorted(secMax_name)

    return secName_sort,friSec_max




def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            ask_name = input("\nEnter a name: ")
            while True:
                if ask_name not in friends_dict:
                    print("\nThe name {} is not in the list.".format(ask_name))
                    ask_name = input("\nEnter a name: ")

                else:
                    value = friends_dict[ask_name]
                    print("\nFriends of {}:".format(ask_name))
                    for d in value:
                        print(d)
                    break


    

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
