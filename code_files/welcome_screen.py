#################################################################################
#                                 VARIABLES                                     #
#################################################################################

s = " "                                                                             # Shortcut for space            
p = "\n"                                                                            # Shortcut for paragraph  
t = "\t"                                                                            # Shortcut for tab



#################################################################################
#                                  MODULES                                      #
#################################################################################

import time                                                                         # Modul for pause the process
import os                                                                           # Modul for setting fond colour

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

def print_welcome_screen(sec):                                                         # Print heading with fond_line-functions and rest it for (seconds)
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


#################################################################################
#                                 MAIN CODE                                     #
#################################################################################
    
print_welcome_screen(2)

