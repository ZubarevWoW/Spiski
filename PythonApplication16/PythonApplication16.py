class Musicians: 
    def __init__(self, number_Musicians, music): 
        self.number_Musicians = number_Musicians 
        self.music = music
   
#создание списка   
list = [] 

#заполнение списка
list.append(Musicians ('БИ-2 -', 'Варвра'))
list.append(Musicians ('Алиса -', 'Родина'))
list.append(Musicians ('Агата Кристи -', 'Моряк'))
list.append(Musicians ('Король и Шут -', 'Лесник'))
list.append(Musicians ('Пикник -', 'Сияние\n'))

print('\t\t\tПриглашенные музыканты и их песни:')
for obj in list:
    print( obj.number_Musicians, obj.music, sep =' ' ) #отправляем указанные объекты текстовым форматом
input('Нажмите Enter, чтобы завершить программу')