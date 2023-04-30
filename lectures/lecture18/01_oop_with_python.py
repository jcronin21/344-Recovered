class Person:
    #this is the constructor: self is always there
    def __init__(self, name, age, first_language='en'):
        self.name = name
        self.age = age
        self.first_language = first_language

#this is the method: all methods have to take self kinda like "this" in java
    def sayGreeting(self):
        if self.first_language == 'en':
            print(self.name, 'says', 'hello')
        elif self.first_language == 'es':
            print(self.name, 'says', 'hola')
        else:
            print('language not known')

        def __setAge(self,newAge):
            self.age =newAge

#create two instances of this class
person1 = Person('Shirly', 67)
person2 = Person('Walter', 67, first_language='es')
person2._setAge(30)
person1.sayGreeting()
person2.sayGreeting()
