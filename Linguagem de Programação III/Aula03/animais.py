class Animal:
    def fazer_som(self):
        pass

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

def main():
    animal1 = Gato()
    animal2 = Cachorro()

    animal1.fazer_som()
    animal2.fazer_som()

if __name__ == "__main__":
    main()