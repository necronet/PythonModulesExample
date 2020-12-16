from base import Base, Persona, Animal

def main():
    b = Base()
    b.message()

    p = Persona()
    p.message()

    a = Animal()
    a.message()

if __name__ == "__main__":
    main()