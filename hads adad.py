import random as r
rand_num=r.randint(1,10)
t=0
print("salam be bazi ma khosh amadid")
vorood=str(input("agar ghasd shoroo bazi ra darid s va agar tozihat ra mikhaid t ra type konid")).lower()
if vorood=="s":
    print("movafagh bashid")
elif vorood=="t":
    print("tozihi nist :)")
for i in range(5):
   t+=1
   adad=int(input("lotfan adad mored nazar khod ra bein 1 ta 10 entekhab konid va faghat 5 bar forsat dari"))
   if 0>adad or adad>11:
       print("adad vared shode bozorg tar az ragham khaste shode ast lotfan dobare talash konid")
       break
   if adad==rand_num:
      print("dorost hads zadi")
   elif adad>rand_num and adad<11:
        print("adadet bozorg tar az mane koochik taresh kon")
   elif adad<rand_num and 0<adad:
        print("adadet koochik tar az mane bozorg taresh kon") 
   if t==5:
       print("bakhti")
       break
print("khodahafez")