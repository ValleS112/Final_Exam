#################################################################################
#                                 VARIABLES                                     #
#################################################################################
process = True                                                                      # Variable for getting a menue system                     
#################################################################################
#                                  MODULES                                      #
#################################################################################

import os
import sys
import time

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################

def print_error(error,sec):                                                             # Print different error codes (code) and rest for (seconds)
    os.system("cls")
    if error == 1:                                                                      # Proof which error code        
        message = "Falsche Eingabe"                                                         # Code if wrong input
    elif error == 2:                                                                    
        message = "Matrizengröße unterschiedlich - Berechnung nicht möglich!"               # Code if uneven size
        
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
                
                if user_input.isdigit():                                                            # Proof user input if integer or restart or return
                    size.append(user_input)
                elif user_input == "###":                                                           # Restart
                    restart = 1
                    break
                elif user_input == "xxx":                                                           # Return
                    back = 1
                    break
                else:                                                                               # Wrong input
                    print_error(1)
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

    if back == 1:                                                                       # Proof if user wants back to main menue
        menue = False
    os.system("cls")                                                                    # Clear window

    


    
#################################################################################
#                                 MAIN CODE                                     #
#################################################################################


while (process):                                                                    # Loop for construct a menue
    start_main_menue()
    get_matrice_size()