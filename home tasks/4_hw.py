# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.
print ('задача 1')
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Метод для вычисления площади
    def S(self):
        return self.width * self.height

    # Метод для вычисления периметра
    def per(self):
        return 2 * (self.width + self.height)

# Создание трех объектов прямоугольника
rect1 = Rectangle(5, 5)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(6, 4)

# Вывод площади и периметра для каждого прямоугольника
print(f"Площадь rect1: {rect1.S()}")
print(f"Периметр rect1: {rect1.per()}")
print(f"Площадь rect2: {rect2.S()}")
print(f"Периметр rect2: {rect2.per()}")
print(f"Площадь rect3: {rect3.S()}")
print(f"Периметр rect3: {rect3.per()}")


# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
print ('задача 2')
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Метод сложение
    def addition(self):
        return self.a + self.b

    # Метод умножение
    def multiplication(self):
        return self.a * self.b

    # Метод деление
    def division(self):
        return self.a / self.b

    # Метод вычитание
    def subtraction(self):
        return self.a - self.b

# Создание объекта
numbers = Math(5, 5)

# Вывод действий
print(f"сложение: {numbers.addition()}")
print(f"умножение: {numbers.multiplication()}")
print(f"деление: {numbers.division()}")
print(f"вычитание: {numbers.subtraction()}")


# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки
print ('задача 3')
class Elements:
    def __init__(self, text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc
    def click(self):
        return f"Клик по кнопке {self.text}"  # Метод для клика по кнопке

# Экземпляры класса
text_box = Elements('Text Box','Кнопка','')
check_box = Elements('Check Box','Кнопка','')
radio_button = Elements('Radio Button','Кнопка','')
web_tables = Elements('Web Tables','Кнопка','')
buttons = Elements('Buttons','Кнопка','')
links = Elements('Links','Кнопка','')
broken_links = Elements('Broken Links','Кнопка','')
upload_download = Elements('Upload/Download','Кнопка','')
dynamic_properties = Elements('Dynamic Properties','Кнопка','')

#вызываем метод
print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links.click())
print(upload_download.click())
print(dynamic_properties.click())