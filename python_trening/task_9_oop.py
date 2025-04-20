# class Button:
#
#     type: str = 'кнопка'
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
#
# #создаем экземпляры класса
# home = Button('домой','/home')
# catalog_msk = Button('каталог','/msk/catalog')
#
# #доступ к атрибутам
# print(home.text)
# print('кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print ('\n') #перенос на другую строку
#
# print(catalog_msk.text)
# print('кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

# class ButtonTwo:
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#     def click(self):
#         return "Клик по локатору - {}".format(self.loc)
#
# #создаем экземпляры класса
# home_two = ButtonTwo('домой','/home','button#home')
#
# #вызываем метод
# print(home_two.click())

# class input:
#     def __init__(self, loc):
#         self.loc = loc
# search = input('input#search')
# print(search.loc)

# class page:
#     def __init__(self, url):
#         self.url = url
#     #метод
#     def get(self):
#         print(self.url)
#
# home = page('страница')
# home.get()

class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    #метод
    def show_my_drink(self):
        if self.ing:
            print(f'газировка и {self.ing}')

        else:
            print('обычная')

drink1 = Soda()
drink2= Soda('малина')
drink1.show_my_drink()
drink2.show_my_drink()