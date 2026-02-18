class dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color

    def speak(self ):
        print("Dog is barking")


dog1=dog("German shepherd", 3,"black")
print(dog1.breed,dog1.age,dog1.color)
dog1.speak()
dog2=dog("Chihuahua",5,"white")
print(dog2.breed,dog2.age,dog2.color)
dog2.speak()
dog3=dog("Malaysia",5,"black")
print(dog3.breed,dog3.age,dog3.color)
