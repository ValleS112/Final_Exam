### Main Code

#Variables

#i = 2   #lines
#k = 2  #colums

#Build matrice
# print("\n")
# for x in range (0,i):
#     for x in range (0,k):
#         print("[ ] ",end="")
#     print("\n",end="")
# print("\n",end="") 


#################################################################################
#                                                                               #
#                           OUTPUT RESULT MATRICE                               #
#                                                                               #
#################################################################################


#################################################################################
#                                  VARIABLES                                    #
#################################################################################

i = 2      # lines
k = 2      # colums
size = i*k    # kind of matrice 
m = "C"

c11 = 8498
c12 = 98
c13 = 84
c21 = 62
c22 = 561
c23 = 651
c31 = 65
c32 = 8
c33 = 548

# #################################################################################
# #                                    LISTS                                      #
# #################################################################################

elements_c = [c11, c12, c13, c21, c22, c23, c31, c32, c33]



# #################################################################################
# #                                  FUNCTIONS                                    #
# #################################################################################
   
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
#                                  MAIN CODE                                    #
#################################################################################

print_matrice("C",2,2,elements_c)
