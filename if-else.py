username = "ibrhmss"
password = 1234

x = str(input("username giriniz: "))
y = int(input("password giriniz: "))

isLoggedin = (username == x) and (password == y)

if (isLoggedin):
    print("Giriş başarılı... ") #-> if komutunu bir koşula bağlamak için kullanırız.
    
else:
    print("Giriş başarısız...")  #-> else koşulumuz karşılanmıyorsa yapılması gerekenleri göstermek için kullanılır.

    
      