#parent/base/superclass
class animal:
    def sound(self ):
        print("Animal is making sound")
#child class/sub class/derived class
class cat(animal):
    def climb(self):
        print("Cat  is climbing a tree")
#child class/sub class/derived class
class cow(animal):
    def chew(self):
        print("Cow is chewing grass")


a=animal()
print(a.sound())

my_cat=cat()
my_cow=cow()
