домашнее задание , выучить ООП на основании этого примера.
# Car - имя класса.  
# Чкертеж робота 

class Car:
    
    # color, brand, speed
    # аргументы класса 
    # какие запчасти у робота и как они выглядят, их характеристики 

    def init(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed
        self.distance = 150
        self.height = 1.5
    
    def makeStep(self):
        self.distance += self.speed

# mersedes - ОБЪЕКТ!!!! 
# создан на основании чертежа Car



mersedes = Car('red', 'mersedes', 10)

print('_bmw distance')
print(mersedes.distance)

# .makeStep() методы обьекта
 
mersedes.makeStep()
mersedes.openDor()
mersedes.beep()



print('_bmw NEW distance')
print(mersedes.distance)