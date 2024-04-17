class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "Pizza"
    #         case "Otter":
    #             return "Something"
    #         case "Jack Russell terrier":
    #             return "Dog"
    #         case _:
    #             return "/"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = Student.get()
    student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    # return Student(name, house, patronus)
    return Student(name, house)


if __name__ == "__main__":
    main()
