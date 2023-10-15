from HairProduct import HairProduct


class Shampoo(HairProduct):
    """Сlass for Shampoo products."""
    def __init__(self, name: str, brand: str, price: float, hair_type: str, volume: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param hair_type: The hair type (wavy, straight, curly, coily)
        :param volume: The volume of the hair (fine, medium, coarse)
        """

        super().__init__(name, brand, price, hair_type)
        self.volume = volume

    def clean(self):
        """Cleans the hair using the shampoo product."""
        print(f"Washing your {self.hair_type} hair with {self._name} gives you a {self.volume} volume.")

    def nourish(self):
        """Nourishes the hair."""
        print(f"{self.get_name()} nourishes {self.hair_type} hair.")


if __name__ == '__main__':
    shampoo = Shampoo('Volume Sensation', 'Kerastas', 2000, 'straight', 'medium')
    shampoo.clean()
    shampoo.nourish()
    shampoo.style()
    shampoo.remove()
