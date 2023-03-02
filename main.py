#n = int(input("Введите n: "))
#sum = q = int(input("Введите q: "))
#d = int(input("Введите d: "))
#while n-1:
    #sum += d
    #n -= 1

print(sum)

b = int(input("Введите число\t"))
q = int(input("Введите число\t "))
n = int(input("Введите число\t" ))
if(q>1):
    S_n = (b*(q**n))/(q-1)
else:
    S_n = (b*(q**n))/(1-q)
print("Сумма первых n членов\t", S_n)