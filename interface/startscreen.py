#################################################################################
#                                 VARIABLES                                     #
#################################################################################

# Variables for fond
symb_fond_1 = "||"
symb_fond_2 = "//"
symb_fond_3 = "\\\\"
space = " "
p="\n"       
t = "\t"
creator=" Creators: Lukas + Valle + Willi"
date="Mrz. 2024"
colour = "\033[92m"
standard = "\033[0m"


#################################################################################
#                                  MODULES                                      #
#################################################################################

import time
import os

#################################################################################
#                                 FUNCTIONS                                     #
#################################################################################
def fond_line_1():
    txt = symb_fond_1+symb_fond_3+2*space+symb_fond_2+symb_fond_1+space\
        +4*symb_fond_1+space\
        +4*symb_fond_1+space\
        +3*symb_fond_1+2*space\
        +symb_fond_1+space\
        +symb_fond_3+4*space+symb_fond_2
    return txt
def fond_line_2():
    txt = symb_fond_1+space+symb_fond_3+symb_fond_2+space+symb_fond_1+space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +3*space+symb_fond_1+4*space\
        +symb_fond_1+3*space+symb_fond_1+space\
        +symb_fond_1+space\
        +space+symb_fond_3+2*space+symb_fond_2
    return txt
def fond_line_3():
    txt = symb_fond_1+6*space+symb_fond_1+space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +3*space+symb_fond_1+4*space\
        +3*symb_fond_1+2*space\
        +symb_fond_1+space\
        +2*space+symb_fond_3+symb_fond_2
    return txt
def fond_line_4():
    txt = symb_fond_1+6*space+symb_fond_1+space\
        +4*symb_fond_1+space\
        +3*space+symb_fond_1+4*space\
        +symb_fond_1+symb_fond_3+4*space\
        +symb_fond_1+space\
        +2*space+symb_fond_2+symb_fond_3
    return txt
def fond_line_5():
    txt = symb_fond_1+6*space+symb_fond_1+space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +3*space+symb_fond_1+4*space\
        +symb_fond_1+space+symb_fond_3+3*space\
        +symb_fond_1+space\
        +space+symb_fond_2+2*space+symb_fond_3
    return txt
def fond_line_6():
    txt = symb_fond_1+6*space+symb_fond_1+space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +3*space+symb_fond_1+4*space\
        +symb_fond_1+2*space+symb_fond_3+2*space\
        +symb_fond_1+space\
        +symb_fond_2+4*space+symb_fond_3
    return txt
def fond_line_7():
    txt = 3*symb_fond_1+space\
        +4*symb_fond_1+space\
        +symb_fond_1+5*space\
        +3*symb_fond_1
    return txt
def fond_line_8_9_11():
    txt = symb_fond_1+5*space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +symb_fond_1+5*space\
        +symb_fond_1
    return txt
        def fond_line_10():
    txt = symb_fond_1+5*space\
        +4*symb_fond_1+space\
        +symb_fond_1+5*space\
        +symb_fond_1
    return txt
def fond_line_12():
    txt = 3*symb_fond_1+space\
        +symb_fond_1+4*space+symb_fond_1+space\
        +3*symb_fond_1+space\
        +3*symb_fond_1
    return txt

#################################################################################
#                                 MAIN CODE                                     #
#################################################################################

print(colour+"\n")
print(fond_line_1())
print(fond_line_2())
print(fond_line_3())
print(fond_line_4())
print(fond_line_5())
print(fond_line_6()+p)
print(t+space+fond_line_7())
print(t+space+fond_line_8_9_11())
print(t+space+fond_line_8_9_11())
print(t+space+fond_line_10())
print(t+space+fond_line_8_9_11())
print(t+space+fond_line_12())
print(standard+"\n")
print(creator+space+"/"+space+date)
print(p)
time.sleep(2)
os.system("cls")

# print("\033[92m"+p)
# for i in range(0,bz):
#     for i in range(0,b):
#         print(space,end="")
#     print(p,end="")
# for i in range(0,z):
#     print(r*symb_frame+(b-2*r)*" "+r*symb_frame)
# for i in range(0,bz):
#     for i in range(0,b):
#         print(space,end="")
#     print(p,end="")
# print("\033[0m"+round(b/4)*" "+creator+" // "+date)
# print(p)


# b=80        #Breite Anzeigefläche
# bz=2        #Breite oberer und unterer Rand
# z=5          #Anzahl Zeilen
# r=3          #Breite Rand
# symb_frame = "*"       #Symbol Rahmen

    


