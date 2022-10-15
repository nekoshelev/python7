
from add import add
import menu
import all_contact
import exit
# Код основной функции
print(".....................................")
print("Добро пожаловать в телефонную книгу")
print(".....................................")
ch = 1
while ch in (1, 2):
    ch = menu.menu()
    if ch == 1:
       add()
    elif ch == 2:
       all_contact.all_contact()
    else:
       exit.exit()
