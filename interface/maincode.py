### Main Code

#Variables

i = 2   #lines
k = 2  #colums

#Build matrice
print("\n")
for x in range (0,i):
    for x in range (0,k):
        print("[ ] ",end="")
    print("\n",end="")
print("\n",end="") 



###Output result matrice
wide=10
# JUST FOR EDIT
c11 = 420
c12 = 564
c13 = 55
c21 = 6684
c22 = 44 
c23 = 5
c31 = 58
c32 = 558
c33 = 47
#JUST FOR EDIT


# BUILD RESULT MATRICE                                                         

l11= len(str(c11)+2*" ") ; l12 = len(str(c12)+2*" ") ; l13 = len(str(c13)+2*" ")                     # Lengths strings elements 1st line
l21= len(str(c21)+2*" ") ; l22 = len(str(c22)+2*" ") ; l23 = len(str(c23)+2*" ")                     # Lengths strings elements 2nd line
l31= len(str(c31)+2*" ") ; l32 = len(str(c32)+2*" ") ; l33 = len(str(c33)+2*" ")                     # Lengths strings elements 3th line

sing_len_1st_line = [l11+l12+l13] ; sum_len_1st_line = sum(sing_len_1st_line)      # Sum lenghts 1st line
sing_len_2nd_line = [l21+l22+l23] ; sum_len_2nd_line = sum(sing_len_2nd_line)      # Sum lenghts 2nd line
sing_len_3rd_line = [l31+l32+l33] ; sum_len_3rd_line = sum(sing_len_3rd_line)      # Sum lenghts 3rd line

if sum_len_1st_line >= sum_len_2nd_line and sum_len_1st_line >= sum_len_3rd_line:
    c_wide = sum_len_1st_line
elif sum_len_2nd_line >= sum_len_1st_line and sum_len_2nd_line >= sum_len_3rd_line:
    c_wide = sum_len_2nd_line
elif sum_len_3rd_line >= sum_len_1st_line and sum_len_3rd_line >= sum_len_2nd_line:
    c_wide = sum_len_3rd_line
c_wide = c_wide - 2

# OUTPUT RESULT MATRICE

print("The result matrice C is: \n"\
     +"\t \u250C"+c_wide*" "+"\u2510 \n"\
     +"    C =\t \u2502"+"  "+"20"+"  "+"200"+"  "+"400 "+"\u2502 \n"\
     +"\t \u2502"+" 45        "+"\u2502 \n"\
     +"\t \u2502"+" 45        "+"\u2502 \n"\
     +"\t \u2514"+c_wide*" "+"\u2518 \n") 
