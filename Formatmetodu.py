#OR1
"""
alfabe = "abcdefgğhıijklmnoöprsştuüvyz"
for i in alfabe:
    print("Bastırılan karakter:{}".format(i))
"""
#OR2
"""
x1 = "Merhaba"
x2 = "Nasılsın"

ifade = "{1} {0}".format(x1,x2)
print(ifade)
"""
#OR3
"""
x1 = "Merhaba"
x2 = "Nasılsın"

ifade = "{1} {0}".format(x1,x2) 
ifade2 = "|{:^15}|".format(x1) #Texti Ortalamak için kullanılıyor.
ifade3 = "|{:<15}|".format(x2) #Texti Sola Yaslamak için Kullanılıyor.
ifade4 = "|{:>15}|".format(x2) #Texti Sağa Yaslamak için kullanılıyor.
ifade5 = "{:b}".format(1024) #Formatın içindeki sayıyı ikilik sistemde yazar.
ifade6 = "{:d}".format(1023) #Formatın içine yalnızca sayısal ifade yazılır.
ifade7 = "{:s}".format("Merhaba") #Formatın içine yalnızca String ifade girilir.

print(ifade)
print(ifade2)
print(ifade3)
print(ifade4)
print(ifade5)
print(ifade6)
print(ifade7)

"""
