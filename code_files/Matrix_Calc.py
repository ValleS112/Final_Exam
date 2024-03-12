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

def print_error(error,sec):                                                         # Print different error codes (code) and rest for (seconds)
    os.system("cls")
    if error == 1:                                                                      # Proof which error code        
        message = "Falsche Eingabe"                                                         # Code if wrong input
    elif error == 2:                                                                    
        message = "Matrizengröße unterschiedlich - Berechnung nicht möglich!"               # Code if uneven size
    elif error == 3:
        message = " Wert 0 nicht möglich!"
    tab = round((100-len("ERROR: "+message))/2)                                         # Formation of error message

    print("\033[91m"+3*"\n"+50*"* "+"\n"                                               
            +tab*" "+"ERROR: "+message+"\n"
            +50*"* "+"\033[0m")                                                         # Print error message
    time.sleep(sec)                                                                     # Rest message for (seconds)                                                                 
    os.system("cls")                                                                    # Clear window

def start_main_menue():                                                             # Output main menue 
    global user_choice                                                                  # Global variable for getting operand as text for printing
    global operand                                                                      # Global vairable for getting operand as integer for processing
    menue = True
    while (menue):                                                                      # Loop for restart input
        os.system("cls")                                                                # Clear window
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
            user_choice= "Matritzen Subtraktion"                                                # Subtraction
            operand = 2
        elif operand == "3":                                                                # Multiplication
            user_choice = "Matritzen Multiplikation"
            operand = 3 
        elif operand == "4":                                                                # Quit programm
            os.system("cls")
            sys.exit(0)
        else:                                                                               # Wrong input
            print_error(1,1.5)

        if operand == 1 or operand == 2 or operand == 3:                                # Proof which selected math operation to continue
            menue = False

    os.system("cls")                                                                    # Clear window
    
def get_matrice_size():                                                             # Start menue for choicing size of matrices 

    global ai                                                                           # Global variable for number of lines of matrix A
    global ak                                                                           # Global variable for number of colums of matrix A
    global bi                                                                           # Global variable for number of lines of matrix B
    global bk                                                                           # Global variable for number of colums of matrix B
    global back                                                                         # Global variable for return to main menue
    restart = 0                                                                         # Local variable for restart

    ai = 0
    ak = 0
    bi = 0
    bk = 0
    menue = True
    while (menue):                                                                      # Loop for restart input

        size = []                                                                           # List for storing numbs of lines and colums to process 
        back = 0
        restart = 0                                                                         # Local variable for restart
        for run_m in range (0,2):                                                           # Loop for getting two different matrices

            for run_r in range (0,2):                                                           # Loop for getting lines and colums of one matrix

                if run_r == 0:                                                                      # Proof which round for output 'line' or 'colum'
                    row = "Zeilenanzahl i"
                else:
                    row = "Spaltenanzahl k"

                print("\n\n\t* * * "+user_choice+" * * * \n"\
                    +"\n\tBitte \033[93m"+row+" der "+str(run_m+1)\
                    +". Matrix\033[0m eingeben \033[91m(NUR GERADE ZAHLEN)\033[0m:\n"\
                    +"\n\t\t   > ### < um Eingabe erneut zu starten "\
                    +"\n\t\t   > xxx < Zurück zum Hauptmenü -\n")                                   # Print request
                                                                    
                user_input = input("\n\t\t\033[94m"+row+"\033[0m der "+"\033[93m"+str(run_m+1)\
                        +". Matrix\033[0m\t=> ")                                                    # User input
                
                if user_input.isdigit() and user_input != "0":                                         # Proof user input if integer or restart or return
                    size.append(user_input)
                elif user_input == "###":                                                           # Restart
                    restart = 1
                    break
                elif user_input == "xxx":                                                           # Return
                    back = 1
                    break
                elif user_input == "0":                                                             # Input 0 is not permitted
                    print_error(3,1.5)
                else:                                                                               # Wrong input
                    print_error(1,1.5)
                    restart = 1                                                                      
                    break
                os.system("cls")                                                                    # Clear window 

            os.system("cls")                                                                    # Clear window
            if restart == 1 or back == 1:                                                       # Proof if user wants restart or return to main menue
                break

        if len(size) == 4 and back != 1 and restart != 1 :                                  # Proof if enough runs and if user want back
             
            ai = int(size[0])                                                                    
            ak = int(size[1])                                                                    
            bi = int(size[2])
            bk = int(size[3])

            if (ai*ak) == (bi*bk) or (ak == bi and operand == 3):                               # Proof if calculation is possible to continue process
                menue = False
            else:                                                                               # Not possible
                print_error(2,1.5)                                                                      

        elif back == 1:                                                                     # Proof if user wants back to main menue
            break

    # if back == 1:                                                                       # Proof if user wants back to main menue
    #     menue = False
    os.system("cls")                                                                    # Clear window
    
def get_matrice_elements(name,mi,mk):                                              # Get elements for matrices from user input with (name of matrice,lines,colums, name of list of elements)
    
    #global elements_m
    global back                                                                             # Global variable for return to main menue
    restart = 0                                                                             # Local variable for restart user input

    elements_m = "elements_"+name                                                   
    globals()[elements_m] = []                                                      # Global list for elements of matrix_m with name "elements_[name]"
    list_elements = []
    back = 0                                                                 
    menue = True    

    while (menue):                                                                       # Loop for getting a menue system
        back = 0
        restart = 0 
        print("\n\n\t* * * Eingabemaske der Matrix-Elemente * * * \n"\
            +"\n\t\tBitte "+"\033[93m"+"Elemente der Matrix "+name+"\033[0m eingeben \033[91m(NUR GERADE ZAHLEN)\033[0m:\n"\
            +"\t\t   > ### < um Eingabe erneut zu starten \n"\
            +"\t\t   > xxx < um zum Hauptmenü zurück \n")                                   # Print input mask
            
        for ri in range (0,mi):                                                             # Loop for getting the right order of elements depend on lines
            for rk in range (0,mk):                                                             # Loop for getting the right order of elements depend on colums
                e = input("\t\t Element: "+str.lower(name)+str(ri+1)+str(rk+1)+"=\t")                                 # User input
                if e.isdigit():                                                                     # Proof if input is an integer, restart or return to main menue 
                    list_elements.append(e)                                                                      
                elif e == "###":                                                                    # Restart                       
                    restart = 1                        
                    break
                elif e == "xxx":                                                                    # Return to main menue
                    back = 1
                    break
                else:                                                                               # Incorrect input 
                    print_error(1,1.5)
                    restart = 1
                    break
            if restart == 1 or back ==1:                                                        # Proof if user wants to return or restart
                break
    
        if restart !=1 or back ==1:                                                         # Proof if user input has finished or if user wants to return to main menue
            globals()[elements_m] = list_elements
            menue = False
        os.system("cls")                                                                    # Clear window

def print_matrice(name,mi,mk,list):                                                 # Print matrice with (name, lines, colums, list of elements)
    
    ex=0                                                                                # Local variable for rotating list elements
    i=1                                                                                 # Local variable

    elements_m = []                                                                     # List for formated elements
    elements_m_lenghts = []                                                             # List for lenghts of elements
    
    for e in range (0,(mi*mk)):                                                         # Proof individual lenght of elements and add to list
        lenght_m_ik = len(str(list[e]))
        elements_m_lenghts.append(lenght_m_ik)

    elements_m_lenghts = sorted(elements_m_lenghts)                                     
    l = elements_m_lenghts[(mi*mk-1)]                                                   # determine greatest lenght, store in variable
        
    for e in range (0,(mi*mk)):                                                         # Formate elements to uniforme lenght 
        m_ik = " "+str(list[e]).rjust(l)
        elements_m.append(m_ik)
    
    m_width = (mk*l+mk)*" "                                                             # Set space between brackets            
    name = name+" = "                                                                   # Formats the name of matrix     
    len_name = len(name)*" "                                                            # Set space between window frame and first bracket
    
    print("\n\t\t"+len_name+"\u250C"+m_width+" \u2510")                               ### Printing matrix       
     
    for run_i in range (0,mi):                                                          # Loop for lines
       
        if run_i == 0:                                                                  # Proof if first line for adding the name of matrix
            print("\t\t"+name,end="")
            i = 0

        print(i*("\t\t"+len_name)+"\u2502",end="")                                        # Print first part of line
        for run_k in range (0,mk):                                                      # Loop for colums
            print(elements_m[(0+ex)],end="")                                                # Print main part of line
            ex = ex + 1   
        print(" \u2502")                                                                # Print last part of line
        i = 1
    print("\t\t"+len_name+"\u2514"+m_width+" \u2518 \n")                                  # Finish of brackets
         



#################################################################################
#                                 MAIN CODE                                     #
#################################################################################
    
print_welcome_screen(2)
process = True
                                                                
while (process):
    back = 0  
    while(back!=1):                                                                 # Loop for construct a menue system
        start_main_menue()                                                          # Main menue
        get_matrice_size()                                                          # User request for input number of lines and colums from matrices
        if back == 1:                                                               # Proof if user wants to return to main menue
            break
        get_matrice_elements("A",ai,ak)                                             # User request for input elements of first matrix
        if back == 1:                                                               # Proof if user wants to return to main menue
            break
        get_matrice_elements("B",bi,bk)                                             # User request for input elements of secon matrix 
        if back == 1:                                                               # Proof if user wants to return to main menue
            break


        print(elements_A)
        os.system("cls")
        print("\n\n"+50*"=")
        print("\n\tThe result matrix C is:")
        print_matrice("C",ai,bk,elements_B)    
        input()
    process = False