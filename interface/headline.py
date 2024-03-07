b=80        #Breite Anzeigefläche
bz=2        #Breite oberer und unterer Rand
z=5          #Anzahl Zeilen
r=3          #Breite Rand
s="*"       #Symbol Rahmen
p="\n"       #Abk. für Absatz
creator=" Creators: Lukas + Valle + Willi"
date="Mrz. 2024"
#Headline
print(p)
for i in range(0,bz):
    for i in range(0,b):
        print(s,end="")
    print(p,end="")
for i in range(0,z):
    print(r*s+(b-2*r)*" "+r*s)
for i in range(0,bz):
    for i in range(0,b):
        print(s,end="")
    print(p,end="")
print(round(b/4)*" "+creator+" // "+date)
print(p)