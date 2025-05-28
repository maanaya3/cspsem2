#Marco Anaya
#init
dogbrd=["Affenpinscher","AfghanHound","AiredaleTerrier","AkbashDog","Akita","AlapahaBlueBloodBulldog","AlaskanHusky","AlaskanMalamute","AmericanEskimoDog","AmericanFoxhound","AmericanPitBullTerrier","AmericanWaterSpaniel","AnatolianShepherdDog","AustralianKelpie","AustralianShepherd","Azawakh","Basenji","BassetBleudeGascogne","Beagle","Beauceron","BedlingtonTerrier","BelgianMalinois","BelgianTervuren","BerneseMountainDog","BlackandTanCoonhound","Bloodhound","BluetickCoonhound","Boerboel","BorderTerrier","BostonTerrier","BouvierdesFlandres","Boxer","BoykinSpaniel","BraccoItaliano","Briard","Brittany","Bullmastiff","CairnTerrier","CaneCorso","CardiganWelshCorgi","CatahoulaLeopardDog","CaucasianShepherd(Ovcharka)","CavalierKingCharlesSpaniel","ChineseCrested","Chinook","ChowChow","ClumberSpaniel","CockerSpaniel(American)","CotondeTulear","Dalmatian","DogoArgentino","EnglishShepherd","EnglishSpringerSpaniel","Eurasier","FieldSpaniel","FinnishLapphund","GermanPinscher","GermanShepherdDog","GermanShorthairedPointer","GiantSchnauzer","GlenofImaalTerrier","GoldenRetriever","GordonSetter","GreatDane","GreatPyrenees","Greyhound","Harrier","Havanese","IrishSetter","IrishWolfhound","ItalianGreyhound","JapaneseChin","Keeshond","Komondor","Kuvasz","LabradorRetriever","LagottoRomagnolo","Leonberger","LhasaApso","Maltese","MiniatureSchnauzer","Newfoundland","NorfolkTerrier","Papillon","PembrokeWelshCorgi","PharaohHound","Plott","Pug","RedboneCoonhound","RhodesianRidgeback","Rottweiler","Samoyed","Schipperke","ScottishDeerhound","ShihTzu","SilkyTerrier","SoftCoatedWheatenTerrier","SpanishWaterDog","Vizsla","Weimaraner"]
minsize=[6,50,40,90,65,55,38,65,20,65,30,25,80,31,35,33,22,35,20,80,17,40,40,65,65,80,45,110,12,10,70,50,25,55,70,30,100,13,88,25,50,80,13,10,50,40,55,20,9,50,80,44,35,40,35,33,25,50,45,65,32,55,45,110,85,50,40,7,35,105,7,4,35,80,70,55,24,120,12,4,11,100,11,3,25,40,40,14,45,75,75,50,10,70,9,8,30,30,50,55]
flist=[]

def dog():
    s=(input("What size dog would you like? A tiny (t) 0-10 dog, a small (s) 11-25 dog, a medium (m) 26-60 dog, or a large (l) dog 60+"))
    if s=="t":
        for i in range(len(minsize)):
            if minsize[i] <=10:
                flist.append(dogbrd[i])
        print(flist)
        print("These are all the tiny dogs in our list")
    if s=="s":
        for i in range(len(minsize)):
            if minsize[i] >10 and minsize[i] <=25:
                flist.append(dogbrd[i])
        print(flist)
        print("These are all the small dogs in our list")
    if s=="m":
        for i in range(len(minsize)):
            if minsize[i] >26 and minsize[i]<=60:
                flist.append(dogbrd[i])
        print(flist)
        print("These are all the medium dogs in our list")
    if s=="l":
        for i in range(len(minsize)):
            if minsize[i] >60:
                flist.append(dogbrd[i])
        print(flist)
        print("These are all the large dogs in our list")


#main
dog()
