class Animal:
    counter = 0
    animals_list = []

    def  __init__(self, weight, age):
        self.weight = weight
        self.age = age

        Animal.counter += 1
        Animal.animals_list.append(self)

    def sleep(self):
        print("To zwierzę śpi")

    def wake_up(self):
        print("To zwierzę wstało")

    def eat(self, food):
        self.food = food
        print("To zwierzę je", self.food)
        self.weight += 1

        self.stop_eating()

    def stop_eating(self):
        print("To zwierzę przestało jeść", self.food)

class Bird(Animal):
    def __init__(self, weight, age, can_fly):
        super().__init__(weight, age)

        self.can_fly = can_fly

    def  can_fly(self):
        if self.can_fly:
            print("To ptak, który potrafi latać")
        else:
            print("To ptak, który nie potrafi latać")

class Mammal(Animal):
    def __init__(self, weight, age, can_swim):
        super().__init__(weight, age)

        self.can_swim = can_swim

    def swim(self):
       if self.can_swim:
            print("To ssak, który potrafi pływać")
       else:
            print("To ssak, który nie potrafi pływać")

class Dog(Mammal):
    def __init__(self, weight, age, can_swim, breed): #rbreed - rasa
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def fetch(self): #fetch - aportować
        print("Ten pies aportuje")

class Cat(Mammal):
    def __init__(self, weight, age, can_swim, breed): #breed - rasa
        super().__init__(weight, age, can_swim)

        self.breed = breed


cat = Cat(8, 30, False, "Perski")
print(cat.weight, cat.age, cat.can_swim, cat.breed)
cat.eat("ryba")
cat.swim()




dog = Dog(10,46,True, "Buldog")
print(dog.weight, dog.age, dog.can_swim, dog.breed)
dog.swim()
dog.eat("kość")
dog.fetch()


bird = Bird(5, 45, True)
print(bird.weight, bird.age, bird.can_fly)
bird.eat("chleb")

mammal = Mammal(5, 45, True)
print(mammal.weight, mammal.age, mammal.can_swim)
mammal.eat("mięso")

# dog = Animal("Pies", 14, 5)
# print(dog.weight)
# dog.eat("rybę")
# print(dog.weight)
#
# cat = Animal("Kot", 12, 3)
# cat.wake_up()
#
# print("Ilość zwierząt:", Animal.counter)
# print("Ilość zwierząt:", Animal.animals_list)
# for index, animal in enumerate(Animal.animals_list):
#     nr = index + 1
#     print('Zwierzę nr',nr)
#     print('Dane o zwierzęciu:')
#     print('gatunek',animal.species)
#     print('waga',animal.weight)
#     print('wiek',animal.age)
#     print('---')