file = open("task2.txt", "r")#открытие файла(вместо имени может быть путь)
nums=[]
while True:#цикл, добавляющий каждую строку файла в массив
    line = file.readline()
    if not line:
        break
    nums.append(int(line))
file.close#закрытие файла
result=10000000#переменная с большим числом для сравнения с итоговым результатом
for i in range(0,len(nums)+1):#цикл поиска решения по минимальному числу ходов
    A=[abs(a - i) for a in nums]
    result_new=sum(A)
    if result>result_new:#условие замены результата на более оптимальный
        result=result_new
print(result)