import timeit


# bilangan = 100
# count =0
# bil1 = 1
# bil2 = 1

# while count < bilangan:
#     mulai = timeit.default_timer()
#     print(bil1,'-->',end=" ")
#     bil_akhir = bil1 + bil2
#     bil1 = bil2
#     bil2 = bil_akhir
#     count += 1
#     selesai = timeit.default_timer()
#     print(selesai-mulai)




def fibo(n):
    if n <= 1:
        return (n)
    else:
        return fibo(n-2) + fibo(n-1)


x = int(input('Suku fibonacci ke :'))
mulai = timeit.default_timer()
for i in range(1, x+1):
    selesai = timeit.default_timer()  
    print(fibo(i),'-->', (selesai-mulai))
    