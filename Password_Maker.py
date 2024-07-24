import random

karakterler = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
a = int(input("Parolanın uzunluğunu giriniz: "))
parola = ""
for i in range (a): 
    parola = parola + random.choice(karakterler) 
print("Şifreniz: ",parola)
