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

    def make_sound(self):
        print("To zwierzę wydaje głos")

class Bird(Animal):
    def __init__(self, weight, age, can_fly):
        super().__init__(weight, age)

        self.can_fly = can_fly

    def  can_fly(self):
        if self.can_fly:
            print("To ptak, który potrafi latać")
        else:
            print("To ptak, który nie potrafi latać")

    def make_sound(self):
        print("Ten ptak śpiewa")

class Mammal(Animal):
    def __init__(self, weight, age, can_swim):
        super().__init__(weight, age)

        self.can_swim = can_swim

    def swim(self):
       if self.can_swim:
            print("To ssak, który potrafi pływać")
       else:
            print("To ssak, który nie potrafi pływać")

    def make_sound(self):
        print("Ten ssak daje głos")


class Dog(Mammal):
    def __init__(self, weight, age, can_swim, breed): #rbreed - rasa
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def fetch(self): #fetch - aportować
        print("Ten pies aportuje")

    def make_sound(self):
        print("Ten pies szczeka")


class Cat(Mammal):
    def __init__(self, weight, age, can_swim, breed): #breed - rasa
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def make_sound(self):
        print("Ten kot miauczy")


animal = Animal(10, 5)
bird = Bird(2, 1, True)
mammal = Mammal(50, 7, False)
dog = Dog(20, 4, True, "Labrador")
cat = Cat(5, 3, False, "Perski")

for animal in animal.animals_list:
    animal.make_sound()
    print("------------")
