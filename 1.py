class Animal:
    counter = 0
    animals_list = []

    def  __init__(self, species, weight, age):
        self.species = species
        self.weight = weight
        self.age = age

        Animal.counter += 1
        Animal.animals_list.append(self)

    def sleep(self):
        print("Ten", self.species, "śpi")

    def wake_up(self):
        print("Ten", self.species, "wstał")

    def eat(self, food):
        self.food = food
        print("Ten", self.species, "je", self.food)
        self.weight += 1

        self.stop_eating()

    def stop_eating(self):
        print("Ten", self.species, "przestał jeść")

dog = Animal("Pies", 14, 5)
print(dog.weight)
dog.eat("rybę")
print(dog.weight)

cat = Animal("Kot", 12, 3)
cat.wake_up()

print("Ilość zwierząt:", Animal.counter)
print("Ilość zwierząt:", Animal.animals_list)
for index, animal in enumerate(Animal.animals_list):
    nr = index + 1
    print('Zwierzę nr',nr)
    print('Dane o zwierzęciu:')
    print('gatunek',animal.species)
    print('waga',animal.weight)
    print('wiek',animal.age)
    print('---')