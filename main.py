class Dog:
    def __init__(self, name, breed, age): #automatically, method's first argument is self (object 자기 자신)
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self, ): #object를 출력하면 (print(object)) 이 메소드가 실행됨
        return f"Puppy named {self.name}, whose breed is {self.breed} and {self.age} years old.\n"
    
    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name} and I am a {self.breed}.")
        self.woof_woof()

    def sleep(self):
        print("zzzzz.......")


class GuardDog(Dog): #경비견의 나이는 언제나 5세
    def __init__(self, name, breed):
        super().__init__(
            name,
            breed,
            5
        )
        self.aggressive = True
    def rrrrr(self):
        print("stay away!")


class Puppy(Dog):  
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1) #super()는 부모 클래스임. 부모 클래스의 initialization을 이용
        self.spoiled = True
        
    def woof_woof(self):
        print("woof woof!")


        
ruffus = Puppy( #instance 생성. instantiation
    name="Ruffus", 
    breed="Beagle"
)
bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian"
)

ruffus.woof_woof()
bibi.rrrrr()
ruffus.sleep()