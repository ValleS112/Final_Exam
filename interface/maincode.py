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
x = i*k    # kind of matrice 

c11 = " "+f"{"280":>4}"
c12 = " "+f"{"20":>4}"
c13 = " "+f"{"20":>4}"
c21 = " "+f"{"2880":>4}"
c22 = " "+f"{"20":>4}"
c23 = " "+f"{"280":>4}"
c31 = " "+f"{"20":>4}"
c32 = " "+f"{"2":>4}"
c33 = " "+f"{"0":>4}"

#################################################################################
#                                    LISTS                                      #
#################################################################################

elements_c = [c11, c12, c13, c21, c22, c23, c31, c32, c33]
lenghts_cik = [] 


#################################################################################
#                                  FUNCTIONS                                    #
#################################################################################

def formate_list(x,list):

    form_cik = " "+f"{"0":>4}"str(list[e])+
        for e in range(0,x)
            list[e].append(form_cik)
    
 

def get_lenght(cik):                        # get lenght of element of C
    lik = len(str(cik))
    return lik
def create_list_lenghts(x):                 # create list with lenghts of Cik
    for e in range(0,(x)):
        l=get_lenght(elements_c[e])
        lenghts_cik.append(l)

def get_c_wide(i,k,list):                   # get the max. lenght of the lines for printing the matrice C
    global c_wide
    l1 = []
    l2 = []
    l3 = []
    lines = [l1, l2, l3]
    e1=0
    en=k

    for l in range (0,i):
        for e in range (e1,en):
            lines[l].append(list[e])

    l1 = sorted(l1)
    l2 = sorted(l2)
    l3 = sorted(l3)
    
    l_l1 = l1[k-1]
    l_l2 = l2[k-1]
    if k == 3:
        l_l3 = l3[k-1]
        lines=[l_l1, l_l2, l_l3]
    else:
        lines=[l_l1, l_l2]

    lines=sorted(lines)
   
    c_wide = (((lines[k-1])-1)*k+2)
   
def print_result_matrice(x, list):          # print result matrice c (wide of matrice / elements from list)
    if x == 4:
        i = 0
    else:
        i = 1
    print(f"\n"+50*"="\
        +"\n\nThe result matrice C is: \n"\
        +"\t \u250C"+c_wide*" "+"\u2510 \n"\
        +"    C =\t \u2502"+list[0]+list[1]+i*(list[2])+"\u2502 \n"\
        +"\t \u2502"+list[3]+list[4]+i*(list[5])+"\u2502 \n"\
        +i*("\t \u2502"+list[6]+list[7]+list[8]+"\u2502 \n")\
        +"\t \u2514"+c_wide*" "+"\u2518 \n")



#################################################################################
#                                  MAIN CODE                                    #
#################################################################################

create_list_lenghts(x)
get_c_wide(i,k,lenghts_cik)
print_result_matrice(x,elements_c)
