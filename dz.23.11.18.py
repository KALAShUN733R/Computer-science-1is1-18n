#Эти команды водять значение
i = int(input("Ведите значение i="))
b = int(input("Ведите значение b="))
#проверка значение i
if i > b:
   # 7 строка производит обмен
    i, b = b, i
    while i < b:
        print(i)
        i = i * i + 1
else:
    while i < b:
        print(i)
        i = i * i + 1