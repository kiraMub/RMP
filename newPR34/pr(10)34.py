print("Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.")
print("Введите стоку целых чисел (через пробел)")
a=str(input()).split() 
for i in range(len(a)): 
   a[i] = int(a[i])
print(sum(a))
