
import math
EPSILON = 0.0000001

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

def factorial(N): 
    check = N.isdigit()
    if check == False:
        return None 

    else:
        n = int(N)
        if n == 0:
            return 1
        else:
            factorials = 1
            for i in range(1,n+1):
                factorials *= i 
    return factorials


def e(): 

    found = 0
    for i in range (11):
        found = found + 1.0/(math.factorial(i))
    founds = float(found)
    round2 = round(founds,10)
    return round2
 

def pi():  

    n = 0 
    m = 0 
    term = 1 
    while abs(term)>= EPSILON:
        n+= 1 
        m += term 
        term= ((-1)**n)/(2*n+1)
    m*= 4
    return round(m,10)
    

   
def sinh(x): 

    try: 
        change_float = float(x)
        n_value= 0 
        value_sinhx = 0 
        term1 = change_float
        while math.fabs(term1) >= EPSILON:
            value_sinhx += term1 
            n_value+=1
            term1 = (change_float**(2*n_value + 1))/ (math.factorial(2*n_value +1))
            
        return round(value_sinhx,10)

    except ValueError:
        return None 
    
    

def main(): 

    print(MENU)
    q = input("\nChoose an option: ")

    checking = q.isalpha()
    while checking == True:

        if q == "F" or q == "f":
            print("\nFactorial")
            num = input("Input non-negative integer N: ")
            z =factorial(num)
            check = num.isdigit()
            if check == False:
                print("\nInvalid N.")
                q = input("\nChoose an option: ")
            else:
                math1 = math.factorial(int(num))
                print("\nCalculated:",z)
                print("Math:",math1)
                print("Diff:",abs(z-math1) )
                q = input("\nChoose an option: ")
        elif q == "E" or q == "e":
            print("\ne")
            x = e()
            change = float(x)
            actual = round(math.e,10)
            difference =(actual -x) 
        
            print("Calculated:", round(x,10))
            print("Math:", actual)
            print("Diff:", '{0:.10f}'.format(difference))
            q = input("\nChoose an option: ")

        elif q == "P" or q == "p":
            print("\npi")
            c =pi()
            actual1 = round(math.pi,10)
            difference1 = actual1 - c
            difference1 = round(difference1,10)
            print("Calculated:", round(c,10))
            print("Math:", actual1)
            print("Diff:", '{0:.10f}'.format(difference1))
            q = input("\nChoose an option: ")

        elif q == "S" or q == "s":
            print("\nsinh")
            radian = input("X in radians: ")
            b = sinh(radian)
            
            try:
                change_var = float(radian)
                actual4= round(math.sinh(change_var),10)
                diff4 = round((actual4 - b),10)
                print("\nCalculated:",b)
                print("Math:",actual4)
                print("Diff: {:.10f}".format(diff4))
                q = input("\nChoose an option: ")
            except ValueError:
                print("\nInvalid X.")
                q = input("\nChoose an option: ")
                

        elif q == "M" or q == "m":
            print(MENU)
            q = input("\nChoose an option: ")
        elif q== "X" or q=="x":
            print("\nThank you for playing.")
            break
        else:
            print("\nInvalid option:", q.upper())
            print(MENU)
            q = input("\nChoose an option: ")

if __name__ == '__main__': 
    main()

        
