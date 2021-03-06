class Dog:
    count = 0  #static vars
    dogs = []

    def __init__(self, name):
        self.name = name
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self):
        print('grrrrrrrrrrrr...woof woof')

    def rollback():                 #Static method made implicitly
        print(Dog.count,Dog.dogs)

    @staticmethod                   #Static method made explicitly
    def jump():
        print(Dog.count,Dog.dogs)
        print("JUMP")



scrappy = Dog("Scrappy")
tommy = Dog("Tommy")
tommy.bark()
Dog.rollback() #calling static methods, unable to call from instance tommy
Dog.jump()      # calling static methods
tommy.jump()    #able to call from instance tommy
