max_n=int(input("Введите размер массива n: "))#задание максимального числа массива n
m=int(input("Введите интервал m: "))#задание интервала m
n=[]
row=[]
for i in range(1,max_n+1):#цикл создающий массив n
    n.append(i)
if m !=1:
    row.append(n[0])#добавление первой единицы в путь
m-=1
max_n-=1
m_new=m
while True:#цикл выполняющий основную функцию
    if m_new>max_n:#условие которое симулирует круговой цикл
        m_new-=(max_n+1)  
    if n[m_new]==1 and len(row)!=0:#условие окончания
        break
    row.append(n[m_new])
    if m==0:
       m_new+=1 
    else:
      m_new+=m  
print('Путь: '+str(row))