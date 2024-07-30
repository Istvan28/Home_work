def view_decorator(view_task):
    def view():
        print("Все доступные задачи тут:")
        view_task()
    
    return view

def create_decorator(gen_task):
    def wrapper(tasks):
        print("Создаем задачку...\n")
        gen_task(tasks)
        print("Задача в файлике))\n")

    return wrapper