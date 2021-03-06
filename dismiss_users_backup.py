import os
import shutil
import time
import distutils
from distutils import util
import distutils.core
print("Разработано для Bingo-Boom.com by SIGNDERTON\n")


# ФУНКЦИОНАЛ #
def cls():
    print("\n" * 100)

def main_menu():
    """ Главное меню """
    print("**********************************************")
    print("*** Добро пожаловать в DISSMIS_USER_SCRIPT ***")
    print("**********************************************\n")
    print("- Введите ЦИФРУ опции для выполнения действия -")
    print("----------------------------------------------")
    print("1. Получить список пользователей для обработки\n")
    print("2. Копировать пользователей в backup$\n")
    print("3. Переместить пользователей в backup$\n")
    print("4. Архивация пользователей в backup$\n")
    print("5. Удаление пользователей из Profile$")
    print("----------------------------------------------")
    print("0. Выход\n\n")
    script_action = input()
    print("Введите число: ")



    # while True:
    #     try:
    #         if script_action == "1":
    #             cls() # Чистим консоль
    #             print("\t*** Читаем список пользователей из файла dissmiss_account_list.txt ***")
    #             script_action = 0
    #             get_list(user_list)
    #             back_to_main()
    #
    #         elif script_action == "2":
    #             cls()  # Чистим консоль
    #             print("*** Копирование пользователей в backup$ ***")
    #             copy(user_list) # Запускаем копирование
    #             back_to_main()
    #
    #         elif script_action == "3":
    #             cls()  # Чистим консоль
    #             print("*** Перемещение пользователей в backup$ ***")
    #             move(user_list)
    #             back_to_main()
    #
    #         elif script_action == "4":
    #             cls()  # Чистим консоль
    #             print("*** Архивация пользователей в backup$ ***")
    #             zip(user_list)
    #             back_to_main()
    #
    #         elif script_action == "5":
    #             cls()  # Чистим консоль
    #             print("*** Удаление пользователей из Profile$ ***")
    #             script_action = 0
    #             delete(user_list)
    #             back_to_main()
    #
    #         else:
    #             cls()  # Чистим консоль
    #             print("*** Ошибка! Выберите существующий вариант! ***")
    #             delete(user_list)
    #             back_to_main()
    #
    #     except:
    #         # Выбор способа оплаты
    #         print('Условия не выполнены')
    #         back_to_main()
    #         # Ошибка, Добавляем кнопки главного меню
    #         pass
    #     finally:
    #         break

    if script_action == "1":
        cls() # Чистим консоль
        print("\t*** Читаем список пользователей из файла dissmiss_account_list.txt ***")
        script_action = 0
        get_list(user_list)
        back_to_main()

    elif script_action == "2":
        cls()  # Чистим консоль
        print("*** Копирование пользователей в backup$ ***")
        copy(user_list) # Запускаем копирование
        back_to_main()

    elif script_action == "3":
        cls()  # Чистим консоль
        print("*** Перемещение пользователей в backup$ ***")
        move(user_list)
        back_to_main()

    elif script_action == "4":
        cls()  # Чистим консоль
        print("*** Архивация пользователей в backup$ ***")
        zip(user_list)
        back_to_main()

    elif script_action == "5":
        cls()  # Чистим консоль
        print("*** Удаление пользователей из Profile$ ***")
        script_action = 0
        delete(user_list)
        back_to_main()

    else:
        cls()  # Чистим консоль
        print("*** Ошибка! Выберите существующий вариант! ***")
        delete(user_list)
        back_to_main()


def  back_to_main():
    print("Для возврата в главное меню введите 0")
    script_action = input()
    if script_action == "0":
        cls()
        main_menu()

def get_list(user_list):
    """ Вывод полученного списка пользователей"""
    print('\nСписок пользователей для работы:\n-------- ')
    for line in user_list:
        print(line)
    print('--------\n\n')
    back_to_main()

def copy(user_list):
    """ КОПИРОВАНИЕ ДИРЕКТОРИЙ ПОЛЬЗОВАТЕЛЕЙ """
    for org in user_list:
        print(org + " копирование...")
        # скопируем все каталоги в созданный
        # копирование дерева  - откуда - куда
        distutils.dir_util.copy_tree(source_path + '/' + org + '', destination_path + org + '', verbose=0)
        print(org + " копирование завершено\n")
    back_to_main()

def move(user_list):
    """ КОПИРОВАНИЕ ДИРЕКТОРИЙ ПОЛЬЗОВАТЕЛЕЙ """
    for org in user_list:
        print(org + " Перемещение...")
        # скопируем все каталоги в созданный
        # копирование дерева  - откуда - куда
        shutil.move('' + source_path + '/' + org + '', destination_path + '/' + org + '')
        print(org + " перемещение завершено\n\n")
        time.sleep(5)
    back_to_main()

def zip(user_list):
    """ АРХИВАЦИЯ ДИРЕКТОРИЙ ПОЛЬЗОВАТЕЛЕЙ """
    for org in user_list:
        print(org + " архивация...")
        shutil.make_archive(backup_path + org, 'zip', destination_path + org + '/')
        print(org + " архивация завершена.\n\n")
        time.sleep(5)
    back_to_main()

def delete(user_list):
    """ УДАЛЕНИЕ ДИРЕКТОРИЙ ПОЛЬЗОВАТЕЛЕЙ"""
    for org in user_list:
        print(org + " Удаление...")
        shutil.rmtree(source_path + '/' + org + '' + '/*')
        print(org + " Удаление завершено")
    back_to_main()
    pass

# ФУНКЦИОНАЛ #


# ОБРАБОТКА ФАЙЛА С ЛОГИНАМИ ПОЛЬЗОВАТЕЛЕЙ # START #
# Название каталогов, которые надо копировать с их содержимым:
with open('dissmiss_account_list', 'r') as dissmiss_users:
    user_list = dissmiss_users.read().split('\n')
# ОБРАБОТКА ФАЙЛА С ЛОГИНАМИ ПОЛЬЗОВАТЕЛЕЙ # END #


# Настройки:
# Путь к основному каталогу откуда надо копировать, а затем удалять
source_path = '//bbstore/Profiles$'

# "//bbstore/backup$/TESTED/source/" #Путь для тестирования скрипта
#\

# Путь к каталогу в который надо копировать
destination_path = "//bbstore/backup$/Profiles/DISSMISS/"
# Путь к каталогу в который сохранять архивы
backup_path = "//bbstore/backup$/Profiles/DISSMISS_ZIP/"
#'//bbstore/backup/Profiles/archive'



if __name__ == '__main__':
    main_menu()
    print("Работа программы завершена!")
