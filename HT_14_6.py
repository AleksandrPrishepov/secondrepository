class Pet:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
            return f"{self.name} бежит, ее возраст {self.age}"
    def jump(self):
            return f"{self.name} прыгает"
    def bithday(self):
            self.age += 1
            print(f"Добавили +1 = {self.age} лет")
    def sleep(self):
            return f"{self.name} спит"

class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        print(f"{self.name} лает")

class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        print(f"Кот мяукает")

class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self, hight):
        print(f"Попугай летает на высоте {hight} метров")

dog1 = Dog("Rex", 9, "Mr.Brown")
print(dog1.run())
print(dog1.jump())
dog1.bithday()
print(dog1.sleep())
dog1.bark()
print()
cat1 = Cat("Киса", 5, "Mr.Brown")
print(cat1.run())
print(cat1.jump())
cat1.bithday()
print(cat1.sleep())
cat1.meow()
print()
parrot1 = Parrot("Попка", 2, "Mr.Brown")
print(parrot1.run())
print(parrot1.jump())
parrot1.bithday()
print(parrot1.sleep())
parrot1.fly(20)


