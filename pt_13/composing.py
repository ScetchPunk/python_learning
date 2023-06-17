class Dog:
    def __init__(self, name, breed, owner):
        """Dog initialisation with name,breed,owner(object)

        Args:
            name (string): Dog's name
            breed (string): Dog's poroda
            owner (Person): The dog's owner
        """
        self.name = name
        self.breed = breed  # порода собаки
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person("Mick Gordon")
stan = Dog("Stanley", "Bulldog", mick)  # последний проп- объект!
print(stan.owner.name)
