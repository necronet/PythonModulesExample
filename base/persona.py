from base.base import Base

class Persona(Base):
    def __init__(self):
        super().__init__()
        print("Constructor of PERSONA class")
        
    def message(self):
        print("I'm a message from PERSONA class")