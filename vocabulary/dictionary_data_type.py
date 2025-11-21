'''sozluk=dict()
sozluk1={}
print(type(sozluk))
print(type(sozluk1))'''

'''peoples={"Melis":20,
         "Mahmut":40,
         3:30,
         "Ali":42,
         "Sude":15,
         "Melike":24,
         "Onur":26
         }
print(peoples["Melis"])
print(peoples["Mahmut"])
print(peoples[3])'''

uyeler={"Uye":["McKaraKule42","Yusuf","Tam1Bela"],
        "Moderator":["XxXBelaXxX","Ela","Onur"],
        "Yoneticiler":["Dark","Yunus","Onur"]}

'''print(uyeler)
print(uyeler["Uye"])
print(uyeler["Moderator"][1])

uyeler["S.Moderator"]=["Ali","Veli"]
print(uyeler)
uyeler["Yoneticiler"].append("Black")
print(type(uyeler["Yoneticiler"]))
print(uyeler["Yoneticiler"])
uyeler["Yoneticiler"].remove("Onur")
print(uyeler["Yoneticiler"])'''

'''while True:
    islem=int(input("1-Kisi Kaldir\n2-Kisi Ekle\n3-Sistemden Cık\nYapmak istediginiz islemi seciniz:\n"))
    if islem == 1:
        yetki=input("Yetkiyi yazınız (Uye,Moderator,Yoneticiler) ")
        if yetki == "Uye":
            print(uyeler["Uye"])
            name=input("Kaldırmak istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].remove(name)
        if yetki == "Moderator":
            print(uyeler["Uye"])
            name=input("Kaldırmak istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].remove(name)
        if yetki == "Yoneticiler":
            print(uyeler["Uye"])
            name=input("Kaldırmak istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].remove(name)
        print(uyeler)
    elif islem == 2:
        yetki = input("Yetkiyi yazınız (Uye,Moderator,Yoneticiler) ")
        if yetki == "Uye":
            print(uyeler["Uye"])
            name=input("Eklemek istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].append(name)
        if yetki == "Moderator":
            print(uyeler["Uye"])
            name=input("Eklemek istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].append(name)
        if yetki == "Yoneticiler":
            print(uyeler["Uye"])
            name=input("Eklemek istediğiniz üyenin takma adini giriniz: ")
            uyeler["Uye"].append(name)
        print(uyeler)
    else:
        break'''

'''uyeler.clear()
print(uyeler)'''

'''takeCopy=uyeler.copy()
print(takeCopy)
takeCopy.clear()
print(uyeler)
print(takeCopy)'''

'''print(uyeler.pop("Moderator"))
print(uyeler)'''

print(uyeler.keys())
print(type(uyeler.keys()))
print(uyeler.values())
print(type(uyeler.values()))

all_users=uyeler.values()
for user in all_users:
    for k in user:
        print(k)

all_users_key=uyeler.keys()
for user in all_users_key:
    print(user)

user_items=uyeler.items()
print(user_items)
print(type(user_items))

for i,j in user_items:
    print(i+"\n----------\n",j)