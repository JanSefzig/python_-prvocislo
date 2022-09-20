
n = int(input("napis cislo: "))
print(n)

for num in range(n + 1):
  
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
         
print("prvni cislo")
x = int(input())
print("zadejte druhe cislo)
y int(input())
print('vysledek : ')
if x + y <= 1000:
      print(x*y)
      else : 
      print(x+y)
