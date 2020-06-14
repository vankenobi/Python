def topla(liste):
        if(len(liste) == 0):
                return 0
        else:
               return liste[0]+(topla(liste[1:]))
print(topla([1,2,3,4]))
