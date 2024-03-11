#################################################################################
#                                 VARIABLES                                     #
#################################################################################
back = 0                                                                            # Variable for return                        
#################################################################################
#                                  MODULES                                      #
#################################################################################

import os
import sys
import time

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################

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

    


    
#################################################################################
#                                 MAIN CODE                                     #
#################################################################################
process = True

while (process):
    start_main_menue()
    get_matrice_size()