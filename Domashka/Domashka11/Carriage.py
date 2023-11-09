class Carriage:
    """Clas that represents Carriage"""
    def __init__(self, number: int):
        """
        :param number: number of carriage
        """
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        """Method that adding passenger"""
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print(f"The carriage {self.number} is already full. There is no space for {passenger}")

    def __len__(self):
        """Method of the passengers quantity"""
        return len(self.passengers)

    def __str__(self):
        """Method that returns the number of the Carriage"""
        return f"[{self.number}]"


class Train:
    """Clas that represents Train"""
    def __init__(self, locomotive):
        """
        :param locomotive: the head of the train
        """
        self.locomotive = "<=[HEAD]"
        self.carriages = []

    def add_carriage(self, carriage):
        """Method that adding carriage"""
        self.carriages.append(carriage)

    def __str__(self):
        """Method that returns the whole train with added carriages"""
        result = f"{self.locomotive}"
        for carriage in self.carriages:
            result += f"-{carriage}"
        return result

    def __len__(self):
        """Method of the carriages quantity"""
        return len(self.carriages)


if __name__ == '__main__':
    carr1 = Carriage(1)
    carr2 = Carriage(2)
    carr3 = Carriage(3)
    carr4 = Carriage(4)

    carr1.add_passenger("Emma")
    carr1.add_passenger("Ethan")
    carr1.add_passenger("Olivia")

    carr2.add_passenger("Liam")
    carr2.add_passenger("Ava")
    carr2.add_passenger("Noah")
    carr2.add_passenger("Mia")
    carr2.add_passenger("Henry")
    carr2.add_passenger("Oliver")
    carr2.add_passenger("Evelyn")
    carr2.add_passenger("Daniel")
    carr2.add_passenger("Oleh")
    carr2.add_passenger("Abbey")
    carr2.add_passenger("Kornelia")

    carr3.add_passenger("Logan")
    carr3.add_passenger("Andrew")

    carr4.add_passenger("Aria")

    train = Train("Inter")
    train.add_carriage(carr1)
    train.add_carriage(carr2)
    train.add_carriage(carr3)
    train.add_carriage(carr4)

    print(train)
    print(f"Numbers of carriages of the train:", len(train))


