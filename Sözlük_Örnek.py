karakter1 = {"Ad":"Musa","Soyad":"Kucuk","Güc":1023,"can":2050}
karakter2 = {"Ad":"Selim","Soyad":"aktas","Güc":1000,"can":2070}


def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Güc"]
    vurulan["can"] = vurulan["can"] - eksilen 

vur(karakter1,karakter2)

print("Karakter1 can degeri:",karakter1["can"])
print("Karakter2 can degeri:",karakter2["can"])
