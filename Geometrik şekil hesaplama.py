def geometri(sekil):
        if(len(sekil) == 3):
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]
                if (a+b) > c and (b+c)>a and (a+c)>b:
                        if (a==b and b==c and c == a):
                                print("Bu bir eşkenar üçgendir.")
                        elif(a == b and b!=c ):
                                print("Bu bir ikizkenar üçgendir.")
                        elif(a!=b and b!=c and c!=a):
                                print("Bu bir çeşitkenar üçgendir.")   
                else:
                        print("Bu bir üçgen değildir.")       
        elif(len(sekil) == 4):
                a = sekil[0]
                b = sekil[1]
                c = sekil[2]
                d = sekil[3]
                if(a==b and a==c and a==d):
                        print("Bu bir karedir.")
                elif(a==c and b==d):
                        print("Bu bir dikdörtgendir.")
                else:
                        print("Normal bir dörtgendir.")      
while(True):
        elemansayisi = int(input("Lutfen eleman sayisini giriniz:"))
        if(elemansayisi == 3):
                a = int(input("birinci kenar giriniz:"))
                b = int(input("ikinci kenar giriniz:"))
                c = int(input("üçüncü kenar giriniz:"))
                geometri([a,b,c])
        elif(elemansayisi == 4):
                a = int(input("birinci kenar giriniz:"))
                b = int(input("ikinci kenar giriniz:"))
                c = int(input("üçüncü kenar giriniz:"))
                d = int(input("dördüncü kenari giriniz:"))
                geometri([a,b,c,d])
        else:
                print("Lütfen tekrar giriniz")
                
