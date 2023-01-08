import time
gunlering = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
gunler = ["pazartesi","salı","carsamba","persembe","cuma","cumartesi","pazar"]
bugun = time.strftime("%A")
while True:
    print("**********************\nbu gun gunlerden",gunler[gunlering.index(bugun)])
    kullanicial = int(input("kac gun sonrasini ogreneceksin  = "))
    kk = kullanicial
    kullanicial = kullanicial + gunlering.index(bugun)
    b = kullanicial%7
    print(f"bu gunden {kk} gun sonra {gunler[b].upper()}")