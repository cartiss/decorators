import datetime
import hashlib
from typing import Callable

def logger_factory(file):
    def logger(func=Callable):
        def new_func(*args, **kwargs):
            with open(file, 'w+', encoding='utf-8') as f:
                f.write(f'Дата и время: {datetime.datetime.now()}\n')
                f.write(f'Название функции: {func.__name__}\n')
                f.write(f'Аргументы функции: {args} и {kwargs}\n')
                f.write(f'Возращаемое значение: {func(*args, **kwargs)}\n')
            #return {'date': datetime.datetime.now(), 'name': func.__name__, 'args': args, 'kwargs': kwargs, 'return_value': func(*args, **kwargs)}
            return func(*args, **kwargs)
        return new_func
    return logger

@logger_factory('logger.txt')
def my_generator(file):
    with open(file, "rb") as f:
        content = f.readlines()
        for line in content:
            try:
                hash_object = hashlib.md5(line)
                yield hash_object.hexdigest()

            except Exception:
                yield "Error"

if __name__ == '__main__':
    var = my_generator('result1.txt')