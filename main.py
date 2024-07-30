from utils import gen_task, update_task, view_task, delete_task 
from files import tasks

def ask():
    while True:
        try:
            print("1. Создать задачу")
            print("2. Обновить задачу")
            print("3. Просмотреть задачу")
            print("4. Удалить задачи")
            print("5. Поиск(Введите ключевое слово: )")
            print("6. Выход")
            user_choice = int(input("Выбери действие: "))
            if user_choice == 1:
                gen_task(tasks)
            elif user_choice == 2:
                update_task()
            elif user_choice == 3:
                view_task()
            elif user_choice == 4:
                delete_task()
            # elif user_choice == 5:

            elif user_choice == 6:
                print("Вы вышли ")
                break
        except ValueError:
            print("Введи номер задачи!!!")


if __name__ == '__main__':
    ask()







    
    
    


