class Dog:
    count = 0  #static vars
    dogs = []

    def __init__(self, name):
        self.name = name
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self):
        print('grrrrrrrrrrrr...woof woof')

    def rollback():                 #Class method made implicitly
        print(Dog.count,Dog.dogs)

    @staticmethod                   #Class method made explicitly
    def jump():
        print(Dog.count,Dog.dogs)
        print("JUMP")



scrappy = Dog("Scrappy")
tommy = Dog("Tommy")
tommy.bark()
Dog.rollback() #calling static methods, unable to call from instance tommy
Dog.jump()      # calling static methods
tommy.jump()    #also unable to call from instance tommy