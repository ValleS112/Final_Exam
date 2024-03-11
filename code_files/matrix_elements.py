#################################################################################
#                                 VARIABLES                                     #
#################################################################################
  
               
#################################################################################
#                                  MODULES                                      #
#################################################################################
import os
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



                    
            
        



get_matrice_elements(i,k)
print_matrice("A",i,k,elements_A)
print_matrice("B",i,k,elements_B)





874
