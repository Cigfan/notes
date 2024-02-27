import os

print ("1 : Создать новый файл заметок")
print ("2 : Отобразить файл заметок")
print ("3 : Добавить текст к файлу заметок")
print ("4 : Удалить файл заметок")
selection = int(input("Введите команду: "))
if selection == 1:
    notes = input("Введите текст: ")
    file = open("Notes.txt","w")
    file.write(notes +"\n")
    file.close()
elif selection == 2:
    file=open("Notes.txt","r")
    print(file.read())
elif selection== 3:
    file=open("Notes.txt","a")
    notes = input("Введите текст: ")
    file.write(notes + "\n")
    file.close()
    file=open("Notes.txt","r")
    print(file.read())
elif selection == 4:
    os.remove("Notes.txt")
else:
    print("Команда не распознана, введите цифру 1, 2, 3 или 4")
