
GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''

def open_file(s):
    
 
    
    file_name = input(("\nInput {} filename: ").format(s))
    while True:
        try:
            fp = open(file_name,"r",encoding ="windows-1252")
            return fp
        except FileNotFoundError:
            print("\nError: No such file; please try again.")
            file_name = input(("Enter file name: ").format(s))

def read_reviews(N,fp):
    newList =[]
    for i in range (N+1):
        newList.append([])
    for i in fp:
        split = i.split()
        userID = int(split[0])
        movieID = int(split[1])
        rating = int(split[2])
        tup = (movieID,rating)
        newList[userID].append(tup)
    
    for i in newList:
        i.sort()

    return newList






def read_users(fp):

    data =[[]]
    for line in fp:
        split = line.strip().split("|")
        reviewer_id = int(split[0])
        age = int(split[1])
        gender = split[2]
        occupation = split[3]
        X_var = split[4]
        tup = (age, gender, occupation)
        data.append(tup)

    return data


def read_movies(fp):

    double_list = [[]]
    for line in fp:
        split = line.strip().split("|")
        title = split[1]
        date = split[2]
        genres = split[5:]
        gen_list = []
        for i in genres:
            gen_list.append(int(i))
        generesNew = []
        for n, var in enumerate(gen_list):
            if var == 1:
                generesNew.append(GENRES[n])
        tup = (title,date,generesNew)
        double_list.append(tup)
    return double_list

  
def year_movies(year,L_movies):

    mainMovie = []
    for i, var in enumerate(L_movies[1:],1):
        day_m_y = var[1]
        try:
            split_day = day_m_y.split("-")[-1]
            valYear = int(split_day)
            if valYear == year:
                mainMovie.append(i)
        except ValueError:
            continue 
    mainMovie.sort()
    return mainMovie
    

def genre_movies(genre,L_movies):

    genre_list = []
    for i, var in enumerate(L_movies[1:],1):
        genre_var = var[2]
        if genre in genre_var:
            genre_list.append(i)
        else:
            continue 
    genre_list.sort()
    return genre_list


def gen_users (gender, L_users, L_reviews):

    gen_list = []
    for i, gender_var in enumerate (L_users[1:],1):
        assign_ele = gender_var[1]
        if assign_ele == gender:
            gen_list.append(L_reviews[i])
        
    return gen_list

def occ_users (occupation, L_users, L_reviews):
    occ_list = []
    for i, occupation_var in enumerate (L_users[1:],1):
        assign_occ = occupation_var[2]
        if assign_occ == occupation:
            occ_list.append(L_reviews[i])
        
    return occ_list


def highest_rated_by_movie(L_in,L_reviews,N_movies):
    findTotal = [0]*len(L_in)
    average_L_in= [0]*len(L_in)
    totalNum_movies = [0]*len(L_in)
    
    for var in range(len(L_in)):
        for i in L_reviews:
            if i != []:
                for c in i:
                    if c[0] == L_in[var]:
                        totalNum_movies[var]+= 1
                        findTotal[var]+= c[1]
    for val in range (len(L_in)):
        try:
            average_L_in[val] = round(findTotal[val]/totalNum_movies[val],2)
        except:
            average_L_in[val]=0
    
    new_list =[]
    new_var = -1 
    for n in range(len(L_in)):
        if average_L_in[n]>new_var:
            new_var= average_L_in[n]
            new_list.append(L_in[n])
            new_list= []
            new_list.append(L_in[n])
        elif average_L_in[n]== new_var:
            new_list.append(L_in[n])

    return new_list, new_var




           
def highest_rated_by_reviewer(L_in,N_movies):
    

    average_RList = []
    
    for i in range (N_movies +1):
        newL = [0,0]
        average_RList.append(newL)
    for n in L_in:
        for tuple in n:
            movieID = tuple[0]
            rating = tuple[1]
            average_RList[movieID][1]+=1 
            average_RList[movieID][0]+= rating
    
    average_list = []
    for m in average_RList:
        m[1]
        m[0]
        try:
            average = m[0]/m[1]
            average_list.append(average)
        except ZeroDivisionError:
            average= 0
            average_list.append(average)
    averageMax = 0 
    for b in average_list:
        if b>averageMax:
            averageMax= b 
    average_movie = []
    for v in range (len(average_list)):
        if average_list[v] == averageMax:
            average_movie.append(v)

    return average_movie,averageMax
    

def main():
    calling_file_users = open_file("users")
    calling_file_reviews = open_file("reviews")
    calling_file_movies = open_file("movies")   
    
    readUsers = read_users(calling_file_users)
    check_length = len(readUsers)+1
    readReviews = read_reviews(check_length,calling_file_reviews)
    readMovies = read_movies(calling_file_movies)
    check_length_movie = len(readMovies)+1

    print(MENU)
    ask_menu = int(input ("\nSelect an option (1-5): "))

    while ask_menu !=5:
        if ask_menu == 1:
            while True:
                try:
                    ask_year = int(input("\nInput a year: "))
                    if ask_year <1930 or ask_year>1998:
                        ask_year = input("\nInput a year: ")
                    else:
                        call_movie = year_movies(ask_year,readMovies)
                        length_movie = len(call_movie)
                        break
                except ValueError:
                    ask_year= input("\nInput a year: ")
            call_rateMovie = highest_rated_by_movie(call_movie,readReviews,length_movie)
            print("\nAvg max rating for the year is:",call_rateMovie[1])
            for i in call_rateMovie[0]:
                print(readMovies[i][0])
            
            

        elif ask_menu ==2:
            print("\nValid Genres are: ",GENRES)
            ask_genres = input("Input a genre: ")
            if ask_genres.capitalize() not in GENRES:
                print("\nError in genre.")
            else:
                calling_genre= genre_movies(ask_genres.capitalize(), readMovies)
                check_length_genre = len(calling_genre)
            calling_high_rated = highest_rated_by_movie(calling_genre,readReviews, check_length_genre)
            print("\nAvg max rating for the Genre is:", calling_high_rated[1])

            for i in calling_high_rated[0]:
                print(readMovies[i][0])
               

        elif ask_menu==3:
            ask_gender = input("\nInput a gender (M,F): ")
            change_upper = ask_gender.upper()
            if change_upper != "M" and change_upper != "F":
                print("\nError in gender.")
                ask_gender = input ("\nInput a gender (M,F): ")
            else:
                ask_gen_user = gen_users(ask_gender,readUsers,readReviews)
                length_of_user= len(ask_gen_user)
                
            ask_high_rev = highest_rated_by_reviewer(ask_gen_user,check_length_movie)
            print("\nAvg max rating for the Gender is:", ask_high_rev[1])

            for i in ask_high_rev[0]:
                print(readMovies[i][0])
        elif ask_menu ==4:
            print("\nValid Occupatipns are: ", OCCUPATIONS)
            ask_occ = input("Input an occupation: ")
            if ask_occ not in OCCUPATIONS:
                print("\nError in occupation.")
                ask_occ = input("Input an occupation: ")
            else:
                call_occ = occ_users(ask_occ,readUsers,read_reviews)

            call_high_rated_occ = highest_rated_by_reviewer(call_occ,check_length_movie)
            print("\nAvg max rating for the occupation is:",call_high_rated_occ)

            for i in ask_high_rev[0]:
                print(readMovies[i][0])

        ask_menu = int(input ("\nSelect an option (1-5): "))
    
    calling_file_users.close()
    calling_file_reviews.close()
    calling_file_movies.close()

if __name__ == "__main__":
    main()
                                           
