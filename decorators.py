import time

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

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result

    return wrapper