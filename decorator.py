#
def decorator1(name_fun1):
    def output_data(*args):
        print("Прізвище: ")
        a = name_fun1(*args)
        print(f"\t{a[1]}")
        print("Ім'я: ")
        a = name_fun1(*args)
        print(f"\t{a[0]}\n")
    return output_data        
#
# @decorator1
# def info(name, surname):
    # return name, surname
# 
# info("Ілюша", "Булочка")
# info("Тоша", "Примуш")
# info("Екатерина", "Крупина")

#
def class_decorator(name_method):
    def output_data(self):
        a = name_method(self)
        print(f"Прізвище:\n\t{a[0]}")
        print(f"Ім'я:\n\t{a[1]}")
        print(f"Вік:\n\t{a[2]}")
    return output_data

class Info:
    def __init__(self, surname, name, age):
        self.SURNAME = surname
        self.NAME = name
        self.AGE = age
    @class_decorator
    def print_info(self):
        return self.SURNAME, self.NAME, self.AGE

info1 = Info("Погребняк", "Нікіта", "14")
info1.print_info()