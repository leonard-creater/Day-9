class Parrot:

    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

franky=Parrot("franky",5)
lois=Parrot("lois",10)

print("franky is a-",franky.species)
print("lois is a-",lois.species)

print(franky.name,franky.age)
print(lois.name,lois.age)