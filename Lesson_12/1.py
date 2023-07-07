# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. ( почти готово)
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. ( готово)
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


import  csv
import  os

myData = [["Geometry"],["Algebra"],["Biology"]]     # создаем список предметов
myFile = open('list_of_items','w')                                 # создаем имя файла csv
with myFile:                                                        # записываем в файл csv
    writer = csv.writer(myFile)
    writer.writerows(myData)

rows =[]
with open('list_of_items', 'r') as csvfile:                     # Читаем из csv файла
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        rows.append(row)
t1 = rows[0]
t2 = rows[2]
t3 = rows[4]
print("Предметы ", t1,t2,t3)
sss = ('*' * 50)
print(sss)

class Range:
    '''Проверяем на вхождение в диапазон по цифрам'''
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, first_name):          # перехватываем имя. которому хотим присвоить значение
        self.param_first_name = '_' + first_name

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance,self.param_first_name,value)

    def validate(self,value):
        if not isinstance(value,int):
            raise TypeError (f'Значение {value} не целое число ')
        if self.min_value is not None and value < self.min_value:
            raise ValueError (f'значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError (f'значение {value} должно быть меньше {self.max_value}')

class Text:
    '''проверяем на заглвную букву в имени, отчестве и фамилии'''
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):          # перехватываем имя. которому хотим присвоить значение
        self.param_name = '_' + name

    def __set__(self, instance, value):             # проверяем на наличие заглавной буквы
        if self.param(value):
            setattr(instance,self.param_name,value)
        else:
            raise ValueError(f'Первая бува не заглавная, либо заглавных букв несколько {value}')


class Letters:
    '''Проверяем на наличие посторонних символов в имени, фамилии и отчестве'''
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):          # перехватываем имя. которому хотим присвоить значение
        self.param_name = name

    def __set__(self, instance, value):             # проверяем на наличие не-букв
        if self.param(value):
            setattr(instance,self.param_name,value)
        else:
            raise ValueError(f'Имя состоит не только из букв {value}')


class Student:
    ''''Ограничиваем диапазон оценок и тестов'''

    score = Range(2, 5 + 1)             # Устанавливаем дапазон оценок
    test = Range (0, 100 + 1)           # Устанавливаем диапазон тестов

    #first_name = Letters (str.isalpha)      # Устанавливаем проверку на не-буквы
    #last_name = Letters (str.isalpha)
    #surname = Letters (str.isalpha)

    #first_name = Text (str.istitle)      # Устанавливаем проверку первой большой буквы
    #last_name = Text (str.istitle)
    #surname = Text (str.istitle)

    def __init__(self, first_name, last_name, surname,
                 score_geometry1, score_geometry2, score_geometry3, test_geometry,
                 score_algebra1, score_algebra2, score_algebra3,  test_algebra,
                 score_biology1, score_biology2, score_biology3, test_biology):
        '''Проводим инициализацию'''
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.score_geometry1 = score_geometry1
        self.score_geometry2 = score_geometry2
        self.score_geometry3 = score_geometry3
        self.test_geometry = test_geometry
        self.score_algebra1 = score_algebra1
        self.score_algebra2 = score_algebra2
        self.score_algebra3 = score_algebra3
        self.test_algebra = test_algebra
        self.score_biology1 = score_biology1
        self.score_biology2 = score_biology2
        self.score_biology3 = score_biology3
        self.test_biology = test_biology

    def display_employee(self):
        #tt = format(self.first_name)
        #tt.istitle()
        #print(tt,tt.istitle())

        sum_geometry = (self.score_geometry1 + self.score_geometry2 + self.score_geometry3) / len(myData)
        sum_algebra = (self.score_algebra1 + self.score_algebra2 + self.score_algebra3) / len(myData)
        sum_biology = (self.score_biology1 + self.score_biology2 + self.score_biology3) / len(myData)

        print('Имя: {}.\nОтчество: {}.\nФамилия: {}.\n'
              'Оценка по {}. :{},{},{}.Средний балл: {}.\nТест по {}. :{}.\n'
              'Оценка по {}. :{},{},{}.Средний балл: {}.\nТест по {}. :{}.\n'
              'Оценка по {}. :{},{},{}.Средний балл: {}.\nТест по {}. :{}.'
              .format(self.first_name, self.last_name, self.surname,
                      t1,self.score_geometry1,self.score_geometry2,self.score_geometry3, sum_geometry,t1,self.test_geometry,
                      t2, self.score_algebra1, self.score_algebra2,self.score_algebra3,sum_algebra,t2, self.test_algebra,
                      t3, self.score_biology1,self.score_biology2,self.score_biology3, sum_biology,t3, self.test_biology))
        print(sss)




    def __repr__(self):                     # Выводим данные об экземпляре класса
        return f'Student (first_name={self.first_name}, last_name={self.last_name}, surname={self.surname}, ' \
               f'score_geometry1= {self.score_geometry1}, score_geometry2= {self.score_geometry2}, score_geometry3= {self.score_geometry3},test_geometry= {self.test_geometry}, ' \
               f'score_algebra1= {self.score_algebra1}, test_algebra= {self.test_algebra},score_biology1 = {self.score_biology1}, test_biology= {self.test_biology})'

if __name__ == "__main__":
    std1 = Student("Ivan","Petrovich", "Petrov",5,4,5,17,4,5,3,65,3,5,5,44)
    std1.display_employee()
