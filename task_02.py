# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def replace_key_value(**kwargs):
    my_dict = dict()
    for k, v in kwargs.items():
        if isinstance(v, (int | float | str | tuple)):
            my_dict[v] = k
        else:
            my_dict[str(v)] = k
    return my_dict


result = replace_key_value(arg1="Hello",
                           arg2=2,
                           arg3="123",
                           arg4=[1, 2, 3, 4, 5])

print(result)
