#################################################################################
#                                 VARIABLES                                     #
#################################################################################
ai = 2
ak = 2
bi = 2
bk = 2               
#################################################################################
#                                  MODULES                                      #
#################################################################################
import os
import time
#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################
def print_error(error,sec):                                                         # Print different error codes (code) and rest for (seconds)
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
    
    print("\n\t"+len_name+"\u250C"+m_width+" \u2510")                               ### Printing matrix       
     
    for run_i in range (0,mi):                                                          # Loop for lines
       
        if run_i == 0:                                                                  # Proof if first line for adding the name of matrix
            print("\t"+name,end="")
            i = 0

        print(i*("\t"+len_name)+"\u2502",end="")                                        # Print first part of line
        for run_k in range (0,mk):                                                      # Loop for colums
            print(elements_m[(0+ex)],end="")                                                # Print main part of line
            ex = ex + 1   
        print(" \u2502")                                                                # Print last part of line
    print("\t"+len_name+"\u2514"+m_width+" \u2518 \n")                                  # Finish of brackets
         


                    

        










