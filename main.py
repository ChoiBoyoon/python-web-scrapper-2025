class Dog:
    def __init__(self, name, breed, age = 0.1): #automatically, method's first argument is self (object 자기 자신)
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self, ): #object를 출력하면 (print(object)) 이 메소드가 실행됨
        return f"Puppy named {self.name}, whose breed is {self.breed} and {self.age} years old.\n"
    
    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name} and I am a baby {self.breed}.")
        self.woof_woof()


class GuardDog(Dog):
    def rrrrr(self):
        print("stay away!")

class Puppy(Dog):  
    def woof_woof(self):
        print("woof woof!")

        
ruffus = Puppy( #instance 생성. instantiation
    name="Ruffus", 
    breed="Beagle"
)
bibi = Puppy(
    name="Bibi",
    breed="Dalmatian"
)

ruffus.introduce()