#################################################################################
#                                 VARIABLES                                     #
#################################################################################

s = " "                                                                             # Shortcut for space            
p = "\n"                                                                            # Shortcut for paragraph  
t = "\t"                                                                            # Shortcut for tab

process = True                                                                      # Variable for menue system   


#################################################################################
#                                  MODULES                                      #
#################################################################################

import time                                                                         # Modul for pause the process
import os                                                                           # Modul for setting fond colour
import sys

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################

def fond_line_1():                                                                  # Creat 1st line of heading
    txt = head_symb_1+head_symb_3+2*s+head_symb_2+head_symb_1+s\
        +4*head_symb_1+s\
        +4*head_symb_1+s\
        +3*head_symb_1+2*s\
        +head_symb_1+s\
        +head_symb_3+4*s+head_symb_2
    return txt
def fond_line_2():                                                                  # ... 2nd line...
    txt = head_symb_1+s+head_symb_3+head_symb_2+s+head_symb_1+s\
        +head_symb_1+4*s+head_symb_1+s\
        +3*s+head_symb_1+4*s\
        +head_symb_1+3*s+head_symb_1+s\
        +head_symb_1+s\
        +s+head_symb_3+2*s+head_symb_2
    return txt
def fond_line_3():                                                                  # ... 3rd line...
    txt = head_symb_1+6*s+head_symb_1+s\
        +head_symb_1+4*s+head_symb_1+s\
        +3*s+head_symb_1+4*s\
        +3*head_symb_1+2*s\
        +head_symb_1+s\
        +2*s+head_symb_3+head_symb_2
    return txt
def fond_line_4():                                                                  # ... 4th line...
    txt = head_symb_1+6*s+head_symb_1+s\
        +4*head_symb_1+s\
        +3*s+head_symb_1+4*s\
        +head_symb_1+head_symb_3+4*s\
        +head_symb_1+s\
        +2*s+head_symb_2+head_symb_3
    return txt
def fond_line_5():                                                                  # ... 5th line...
    txt = head_symb_1+6*s+head_symb_1+s\
        +head_symb_1+4*s+head_symb_1+s\
        +3*s+head_symb_1+4*s\
        +head_symb_1+s+head_symb_3+3*s\
        +head_symb_1+s\
        +s+head_symb_2+2*s+head_symb_3
    return txt
def fond_line_6():                                                                  # ... 6th line...
    txt = head_symb_1+6*s+head_symb_1+s\
        +head_symb_1+4*s+head_symb_1+s\
        +3*s+head_symb_1+4*s\
        +head_symb_1+2*s+head_symb_3+2*s\
        +head_symb_1+s\
        +head_symb_2+4*s+head_symb_3
    return txt
def fond_line_7():                                                                  # ... 7th line...
    txt = 3*head_symb_1+s\
        +4*head_symb_1+s\
        +head_symb_1+5*s\
        +3*head_symb_1
    return txt
def fond_line_8_9_11():                                                             # ... 8th/9th/11th line...
    txt = head_symb_1+5*s\
        +head_symb_1+4*s+head_symb_1+s\
        +head_symb_1+5*s\
        +head_symb_1
    return txt
def fond_line_10():                                                                 # ... 10th line...
    txt = head_symb_1+5*s\
        +4*head_symb_1+s\
        +head_symb_1+5*s\
        +head_symb_1
    return txt
def fond_line_12():                                                                 # ... 12th line...
    txt = 3*head_symb_1+s\
        +head_symb_1+4*s+head_symb_1+s\
        +3*head_symb_1+s\
        +3*head_symb_1
    return txt

def print_welcome_screen(sec):                                                      # Print heading with fond_line-functions and rest it for (seconds)
    global head_symb_1                                                                  # Global shortcut for symbol for creating heading
    global head_symb_2                                                                  # Global shortcut for symbol for creating heading
    global head_symb_3                                                                  # Global shortcut for symbol for creating heading
    creator=" Creators: Lukas + Valentin + Willi "                                      # Setcreator's name
    date="Mrz. 2024"                                                                    # Set date of release
    colour = "\033[92m"                                                                 # Setfond colour
    standard = "\033[0m"                                                                # Set standard fond colour
    head_symb_1 = "||"                                                                  # Set symbol for creating heading
    head_symb_2 = "//"                                                                  # Set symbol for creating heading
    head_symb_3 = "\\\\"                                                                # Set symbol for creating heading
    print(colour+"\n")                                                                ### Print welcome screen  
    print(fond_line_1())
    print(fond_line_2())                                                                    #
    print(fond_line_3())
    print(fond_line_4())                                                                    #
    print(fond_line_5())
    print(fond_line_6()+p)                                                                  #
    print(t+s+fond_line_7())
    print(t+s+fond_line_8_9_11())                                                           #
    print(t+s+fond_line_8_9_11())
    print(t+s+fond_line_10())                                                               #
    print(t+s+fond_line_8_9_11())
    print(t+s+fond_line_12())                                                               #
    print(standard+"\n")
    print(creator+s+head_symb_3+s+date)
    print(p)                                                                          ### Print welcome screen
    time.sleep(sec)                                                                     # Rest welcome screen for (seconds)
    os.system("cls")                                                                    # Clear window

def print_error(error):                                                             # Print different error codes (code) 
    os.system("cls")
    if error == 1:                                                                      # Proof which error code        
        message = "Falsche Eingabe"                                                         # Code if wrong input
    elif error == 2:                                                                    
        message = "Matrizengröße unterschiedlich - Berechnung nicht möglich!"               # Code if uneven size
        
    tab = round((100-len("ERROR: "+message))/2)                                         # Formation of error message

    print("\033[91m"+3*"\n"+50*"* "+"\n"                                               
            +tab*" "+"ERROR: "+message+"\n"
            +50*"* "+"\033[0m")                                                         # Print error message
    time.sleep(1.5)                                                                     # Rest message for (seconds)                                                                 
    os.system("cls")                                                                    # Clear window
    
def start_main_menue():                                                             # Output main menue 
    global user_choice                                                                  # Global variable for getting operand as text for printing
    global operand                                                                      # Global vairable for getting operand as integer for processing
    menue = True
    while (menue):                                                                      # Loop for restart input
        print("\n\n\t* * * Willkommen bei unserem Matrizen-Rechner * * * \n"             
            +"\n\t\tHauptmenü - Bitte wählen Sie aus:\n\n"
            +"\t\t  (1) Matritzen Addition\n"
            +"\t\t  (2) Matritzen Subtraktion\n"
            +"\t\t  (3) Matritzen Multiplikation\n"
            +"\n\t\t   - (4) Beenden -\n")                                              # Print main menue
        operand = str(input("\t\tIhre Wahl:\t=> "))                                     

        if operand == "1":                                                              # Proof input which option selected
            user_choice = "Matritzen Addition"                                              # Addition
            operand = 1
        elif operand == "2":
            operand= "Matritzen Subtraktion"                                                # Subtraction
            operand = 2
        elif operand == "3":                                                                # Multiplication
            user_choice = "Matritzen Multiplikation"
            operand = 3 
        elif operand == "4":                                                                # Quit programm
            os.system("cls")
            sys.exit(0)
        else:                                                                               # Wrong input
            print_error(1)

        if operand == 1 or operand == 2 or operand == 3:                                # Proof which selected math operation to continue
            menue = False

    os.system("cls")                                                                    # Clear window
    
def get_matrice_size():                                                             # Start menue for choicing size of matrices 
    global size_A                                                                       # Global variable for size of matrice A
    global size_B                                                                       # Global variable for size of matrice B
    global back                                                                         # Global variable for return to main menue
    back = 0
    menue = True
    while (menue):                                                                      # Loop for restart input
        size = []                                                                           # List for storing selected size to process        
        for run in range (0,2):                                                             # Loop for getting two different inputs
            print("\n\n\t* * * "+user_choice+" * * * \n"\
                +"\n\t\tBitte Größe der "+"\033[93m"+str(run+1)+". Matrix\033[0m wählen:\n\n"\
                +"\t\t  (1) 2x2 Matrix\n"\
                +"\t\t  (2) 3x3 Matrix\n"\
                +"\n\t\t   - (3) Zurück zum Hauptmenü -\n")                                     # Print menu for size slection
            choice = str(input("\n\t\tGröße der "+"\033[93m"+str(run+1)\
                        +". Matrix\033[0m\t=> "))                                               # User input
            size.append(choice)                                                                 # Add user input to list 
            if size[run] == "1":                                                                # Proof user input which size selected 
                size[run] = 2                                                                       # 2x2 matrix
            elif size[run] == "2":
                size[run] = 3                                                                       # 3x3 matrix
            elif size[run] == "3":        
                os.system("cls")                                                                    # Back to main menue
                back = 1
                break
            else:
                print_error(1)                                                                      # Wrong input
                size.pop()
                break
                
            os.system("cls")                                                                    # Clear window

        if len(size) == 2 and back != 1:                                                    # Proof if enough runs and if user want back 
            size_A = size[0]                                                                    # determine size of matrix A 
            size_B = size[1]                                                                    # determine size of matrix A

            if size_A == size_B:                                                                # Proof if matrices have same size to continue process
                menue = False                                                                       # Same size
            else:
                print_error(2)                                                                      # Uneven size
        if back == 1:                                                                       # Proof if user wants back to main menue
            break
    os.system("cls")                                                                    # Clear window
    
def get_matrice_elements(i,k):                                                      # Get elements for matrices from user input
    global back                                                                         # Global variable for return to main menue
    back = 0                                                                 
    elements = True
    while (elements):                                                                   # Loop for getting a menue system
        global elements_A                                                                   # Global lists for elements of A
        global elements_B                                                                   # Global lists for elements of A 
        elements_A= []  
        elements_B= []
        new = 0                                                                             # Local variable for restart user input
        
        for run in range (0,2):                                                             # Loop for getting two different lists
            print("\n\n\t* * * Eingabemaske der Matrix-Elemente * * * \n"\
                +"\n\t\tBitte "+"\033[93m"+"Elemente der "+str(run+1)+". Matrix\033[0m eingeben:\n"\
                +"\t\t   > ### < um Eingabe erneut zu starten \n"\
                +"\t\t   > xxx < um zum Hauptmenü zurück \n")                                   # Print input mask
            
            if (run+1) == 1:                                                                    # Proof run for determine list name
                m = "a"
                list = elements_A
            else:
                m= "b"
                list = elements_B

            for ri in range (0,i):                                                              # Loop for getting the right order of elements depend on lines
                for rk in range (0,k):                                                              # Loop for getting the right order of elements depend on colums
                    e = input("\t\t Element: "+m+str(ri+1)+str(rk+1)+"=\t")                             # User input
                    if e.isdigit():                                                                     # Proof if input is an integer 
                        list.append(e)                                                                      # Add to list
                    elif e == "###":                                                                    # Proof if input is code for restart                        
                        new = 1                        
                        break
                    elif e == "xxx":                                                                    # Proof if input is code for return to main menue
                        back = 1
                        break
                    else:                                                                               # Proof if incorrect input 
                        print_error(1)
                        new = 1
                        break
                if new == 1 or back ==1:                                                            # Proof if user wants to return or restart
                    break       
            os.system("cls")                                                                        # Clear window                
            if new == 1 or back == 1:                                                           # Proof if user wants to return or restart
                break
        if new !=1 or back ==1:                                                             # Proof if user input has finished or if user wants to return to main menue
            elements = False

def print_matrice(name,i,k,list):                                                       # Print matrice with (name, lines, colums, list of elements)
    elements_m = []                                                                         # List for formated elements
    elements_m_lenghts = []                                                                 # List for lenghts of elements
    
    for e in range (0,(i*k)):                                                               # Proof individual lenght of elements and add to list
        lenght_m_ik = len(str(list[e]))
        elements_m_lenghts.append(lenght_m_ik)
    elements_m_lenghts = sorted(elements_m_lenghts)                                         # Sort elements of list
    l = elements_m_lenghts[(i*k-1)]                                                         # determine greatest lenght, store in variable
        
    for e in range (0,(i*k)):                                                               # Formate elements to uniforme lenght 
        m_ik = " "+str(list[e]).rjust(l)
        elements_m.append(m_ik)
    
    m_width = (k*l+k+1)*" "                                                                 # Parameter for printing matrice           
    list = elements_m                                                                       # Parameter for printing matrice
    if (i*k) == 4:                                                                          # Proof if 2x2 or 3x3 matrice
        ex = 0
    else: 
        ex = 1

    print("\t \u250C"+m_width+"\u2510 \n"\
        +"    "+name+" =\t \u2502"+list[0]+list[1]+ex*(list[(ex*2)])+" \u2502 \n"\
        +"\t \u2502"+list[(2+ex)]+list[(3+ex)]+ex*(list[(ex*5)])+" \u2502 \n"\
        +ex*("\t \u2502"+list[(ex*6)]+list[(ex*7)]+list[(ex*8)]+" \u2502 \n")\
        +"\t \u2514"+m_width+"\u2518 \n")                                                   # Print matrice 
  

#################################################################################
#                                 MAIN CODE                                     #
#################################################################################
    
print_welcome_screen(2)
process = True                                                                  
while (process):                                                                    # Loop for construct a menue system
    start_main_menue()
    get_matrice_size()
    get_matrice_elements(i,k)
    
    