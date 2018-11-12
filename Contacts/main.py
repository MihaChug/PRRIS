## -*- coding: utf-8 -*-
contacts = []
command = ""
find = 0
print 'If you want to exit - print "exit"'
while command != "exit":
    command = raw_input(">")
#Добавляем новый контакт в конец списка c учетом всех возможных сочетаний начальных букв с первой по последнюю
    if command[0:3] == 'Add':
        for i in range(len(command[3:]) - 1):
            contacts.append(command[4:i+5])
#Ищем все вхождения элементов в списке
    elif command[0:4] == 'Find':
        find = contacts.count(command[5:])
        print "-> ", find
    elif command != 'exit':
        print "Wrong command!"


