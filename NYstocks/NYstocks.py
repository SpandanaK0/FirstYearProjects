import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''Docstring'''

    ask_file = input("\nEnter the price's filename: ")

    while True:
        try:
            priceFile= open(ask_file)
            break
        except:
            print("\nFile not found. Please try again.")
            ask_PriceFile = input("\nEnter the price's filename: ")

    while True:
        ask_SecurityFile = input("\nEnter the security's filename: ")
        try:
            securityFile= open(ask_SecurityFile)  
            break
        except:
            print("\nFile not found. Please try again.")
            ask_SecurityFile = input("\nEnter the security's filename: ")
             
    return priceFile, securityFile

def read_file(securities_fp):
 
    readingS = csv.reader(securities_fp)

    next(readingS,None)
    dic={}
    name_set = set()
    for i in readingS:
        key = i[0]
        name=(i[1])
        sector=i[3]
        subsector=i[4]
        address=i[5]
        date_add=i[6]
        emptyL=[]
        name_set.add(name)
        finalL= [name,sector,subsector,address,date_add,emptyL]
        dic[key]= finalL
    return name_set, dic
        
def add_prices (master_dictionary, prices_file_pointer):

    readingP= csv.reader(prices_file_pointer)
    next(readingP,None)
    for n in readingP:
        date = n[0]
        comp_name =n[1]
        open_info = float(n[2])
        close_info = float(n[3])
        low_info = float(n[4])
        high_info= float(n[5])
        price_final = [date,open_info,close_info,low_info,high_info]
        
        if comp_name not in master_dictionary:
            continue
        master_dictionary[comp_name][5].append(price_final)
    
        


    
def get_max_price_of_company (master_dictionary, company_symbol):
    emptyL= []
    if company_symbol not in master_dictionary:
        return (None,None)
    newL= master_dictionary[company_symbol][5]
    if newL == []:
        return(None,None)
    for i in newL:
        max_price = i[4]
        date = i[0]
        emptyL.append((max_price,date))
        max_num = max(emptyL)
        
    return max_num
    

def find_max_company_price (master_dictionary):
    newList = []
    for i in master_dictionary:
        max_vals,date = get_max_price_of_company(master_dictionary,i)
        if max_vals != None and date!= None:
            newList.append((max_vals,i))
        find_max,find_symbol = max(newList)
    return(find_symbol,find_max)

        
def get_avg_price_of_company (master_dictionary, company_symbol):
    empL= []
    if company_symbol not in master_dictionary:
        return 0.0
    
    newL= master_dictionary[company_symbol][5]
    if newL == []:
        return 0 
    for i in newL:
        high_price = float(i[4])
        empL.append(high_price)
    length = len(empL)
    find_mean = round(sum(empL)/length,2)

    return find_mean
            
def display_list (lst):  

    count =1 
    for i in lst:

        if count == 3:
            print("{:^35s}".format(i))
            count = 1
        else: 
            print("{:^35s}".format(i),end='')
            count += 1
    print("\n")
    
def main():
    print("Welcome to the New York Stock Exchange.\n")
    priceFile,securityFile =open_file()
    print(MENU)
    ask_option = input("\nOption: ")
    name_val, read_dic = read_file(securityFile)
    add_prices(read_dic,priceFile)

    while ask_option!= "6":

        if ask_option == "1":
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            name_list = sorted(list(name_val))
            display_list(name_list)

        if ask_option =="2":
            print("\ncompanies' symbols:")
            compSymList = []
            for i in read_dic:
                compSymList.append(i)
            compsymSorted = sorted((compSymList))
            display_list(compsymSorted)
            
        if ask_option == "3":
            ask_maxPrice = input("\nEnter company symbol for max price: ")
            if ask_maxPrice not in read_dic:
                print("\nError: not a company symbol. Please try again.")
                ask_maxPrice = input("\nEnter company symbol for max price: ")
            call_maxPrice = get_max_price_of_company(read_dic,ask_maxPrice)
            if call_maxPrice[0] == None:
                print("\nThere were no prices.")
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(call_maxPrice[0],call_maxPrice[1]))
            
        if ask_option == "4":
            call_findMax = find_max_company_price(read_dic)
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(call_findMax[0],call_findMax[1]))

        if ask_option =="5":
            ask_avgPrice = input("\nEnter company symbol for average price: ")
            if ask_avgPrice not in read_dic:
                print("\nError: not a company symbol. Please try again.")
                ask_avgPrice = input("\nEnter company symbol for average price: ")
            call_avgPrice = get_avg_price_of_company(read_dic,ask_avgPrice)
            print("\nThe average stock price was ${:.2f}.\n".format(call_avgPrice))

        print(MENU)  
        ask_option = input("\nOption: ")

if __name__ == "__main__": 
    main() 
