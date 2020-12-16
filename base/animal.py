from base import Base

class Animal(Base):
    def __init__(self):
        super().__init__()
        print("Constructor of ANIMAL class")
        
    def message(self):
        print("I'm a message from ANIMAL class")