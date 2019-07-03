zırhlar = {"demir":10,"celik":20}
karakterler = {"karakter1":{"silah":"kılıç","güç":30,"saglık":100,"zırh":zırhlar["demir"]},
               "karakter2":{"silah":"kılıç","güç":40,"saglık":100,"zırh":zırhlar["celik"]}
              }
def vur(saldiran:dict,saldirilan:dict):
    güç = saldiran["güç"]
    saglik = saldirilan["saglık"]
    zırh = saldirilan["zırh"]
    damage = güç - zırh
    saglik -= damage
    saldirilan["saglık"] = saglik
print(karakterler["karakter1"]["saglık"])
print(karakterler["karakter2"]["saglık"])
vur(karakterler["karakter1"],karakterler["karakter2"])
print(karakterler["karakter1"]["saglık"],karakterler["karakter2"]["saglık"])
