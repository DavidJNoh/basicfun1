class animal:
    def __init__(self, name, health):
        self.name=name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayhealth(self):
        print("Name:"+str(self.name), "Health:"+str(self.health))
        return self


class dog(animal):
    def __init__(self,name,health=0):
        super().__init__(name,health)
        self.health=150
    def pet(self):
        self.health+=5
        return self


class dragon(animal):
    def __init__(self,name,health=0):
        super().__init__(name,health)
        self.health=170
    def fly(self):
        self.health-=10
        return self
    def displayhealth(self):
        super().displayhealth()
        print("I am a Dragon")

# greg= animal("Greg", 100)

# greg.run().run().walk().pet().pet().pet().pet().pet().pet().pet().pet().pet().displayhealth()
# greg.displayhealth()
# dog1= dog("creativename")
# dog1.walk().walk().walk().run().run().pet().displayhealth()
# dog1.fly().displayhealth()

# me=dragon("dankmemes")
# me.fly().displayhealth()

