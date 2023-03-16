# class MyException(Exception):  # создаём пустой класс – исключения
#     pass
#
#
# try:
#     raise MyException("My Message")  # поднимаем наше исключение
# except MyException as e:
#     print(e)
#
#
# class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
#     pass
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     pass
#
# try:
#     raise ChildException("Mmmmmessage")  # поднимаем исключение-наследник
# except ParentException as e:  # ловим его родителя
#     print(e)

class ParentException(Exception):
    def __init__(self, message,
                 error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)


try:
    raise ChildException("message", "Sup error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    pass
    print(e)  
