#удалить пустые строки из списка

list1 = ["The", "", "", "quick", "", "", "brown", "", "fox", ""]
new_list = []
for i in list1:
    if i != "":
        new_list.append(i)
print(new_list)

#дан список из чисел, првратить его в список из квадратов этих чисел

list2 = []
for num in range (5):
    a = int(input('Введите число:  '))
    c = a**2
    list2.append(c)
print(list2)

# дан список, удалить из него все встречающиеся 20

list3 = [1, 20, 2, 3, 4, 20, 2, 20]
for i in list3:
    if i == 20:
        list3.remove(20)
print(list3)

#вывести список в обратной последовательности

list4 = [1, 2, 3, 3, 5]
list4.reverse()
print(list4)

#поменять местами самый большой и маленький элементы списка

List5=[1, 2, 6, 9, 3]
i = list5.index(max(s))
j = list5.index(min(s))
list5[i], list5[j] = list5[j], list5[i]
print(list5)

#вывести повторяющиеся элементы списка

list6 = ['a', 'b', 'a', 'c', 'b', 'a']
for i in set(list6):
    if list6.count(i) > 1:
         print(i)

#найти сумму и произведение элементов списка

list7 = [1, 2, 3, 4]
s, pr = 0, 1
for i in list7:
   s += i
   pr *= i
print('Сумма элементов  ', s)
print('Произведение элементов  ', pr)