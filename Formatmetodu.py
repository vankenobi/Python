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

print(ifade)
print(ifade2)
print(ifade3)
print(ifade4)
"""
