#Random Password Generator
#
# Generate random password and display the result on user interface.
# So that I can generate my password for any application.
#
# Acceptance Criteria:
#
#     Password length must be 10 characters long.
#     It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
#     You must import some required modules or packages.
#     The GUI of program must contain at least a button and a label.
#     The result should be display on the password label when the user click the generate button.


import random
import string
num=string.digits
sembol=string.punctuation
letter_s=string.ascii_lowercase
letter_up=string.ascii_uppercase
alles=[num,sembol,letter_s,letter_up]
password=""
for i in range (3):
    password +=alles[0][random.randint(0,11)]
for i in range (3):
    password +=alles[1][random.randint(0,11)]
for i in range (2):
    password +=alles[2][random.randint(0,11)]
for i in range (2):
    password +=alles[3][random.randint(0,11)]    
print("Your password is = ",password)




# 3- Number Guessing Game

# As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. So that I can try to find the correct number which was selected by computer.

# Acceptance Criteria:

#     Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
#     Your program should prompt the user for guesses
#     if the user guesses incorrectly, it should print whether the guess is too high or too low.
#     If the user guesses correctly, the program should print total time and total number of guesses.
#     You must import some required modules or packages
#     You can assume that the user will enter valid input.

import random
import time


minimum = int(input("En kucuk rakami giriniz: "))
maximum = int(input("En buyuk rakami giriniz: "))
target = random.randint(minimum, maximum)

print("Ai bir numara secti")

n = 1  

time1 = time.time()
while True:
    predict = int(input("Tahmin et bakalim: "))
    if predict == target:
        print("Tebrikler!")
        break                                                
    elif predict > target:  
        print("Kucuk bir numara deneyiniz: ")
        n += 1
    elif predict < target:
        print("Buyuk bir numara deneyiniz: ")
        n += 1
    continue  
time2 = time.time() 
duration = float(time2 - time1)

print("Gecen zaman: {} saniye". format(duration))
print("Deneme sayisi: {}". format(n))



#4-Dort islem yapan bir hesap makinasi yapiyoruz


print("Hangi islemi yapmak istersiniz?")
print("1.Toplama","2.Cikarma","3.Bolme","4.Carpma")
while True:
  Secim=input("Seciminiz Yazin:")
  sayi1=float(input("Lutfen bir tane sayi girin:"))
#if sayi1!=float :
 #   print("Lutfen kusurlu sayi girin!")
  sayi2=float(input("Lutfen 2. sayiyi girin:"))

#if sayi2!=float :   
 #    print("Lutfen tamsayi sayi girin!")
  if Secim=="1":
     print(sayi1,"+",sayi2,"=",sayi1+sayi2)
  elif Secim=="2":
    print(sayi1,"-",sayi2,"=",sayi1-sayi2)    
  elif Secim=="3":
    print(sayi1,"/",sayi2,"=",sayi1//sayi2)
  elif Secim=="4":
    print(sayi1,"*",sayi2,"=",sayi1*sayi2)    
  else:
    print("hatali giris yaptiniz.!")
  devam=input("Devam etmek isterseniz Y,Bitirmek icin N basin!") 
  if devam=="Y":
    continue
  elif devam=="N" :
    break
  else:
    print("Hesaplamamiz burada bitti.")
    break
    