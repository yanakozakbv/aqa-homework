from MakeupProduct import MakeupProduct


class Mascara(MakeupProduct):
    """Сlass for Mascara products."""
    def __init__(self, name: str, brand: str, price: float, makeup_type: str, waterproof: bool):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param makeup_type: The make-up type (lashes, lips etc.)
        :param waterproof: Yes or no
        """
        super().__init__(name, brand, price, makeup_type)
        self.waterproof = waterproof

    def enhance(self):
        """Checking the waterproof"""
        if self.waterproof:
            print(f"Applying {self._name} to make your {self.makeup_type} waterproof.")
        else:
            print(f"Applying {self._name} to enhance your {self.makeup_type} look.")

    def volumize(self):
        """Provides volume to the eyelashes."""
        print(f"{self.get_name()} volumizes your eyelashes.")


if __name__ == '__main__':
    mascara = Mascara('Grandirose', 'Lancome', 700, 'mascara', True)
    mascara.enhance()
    mascara.volumize()
    print(mascara.get_name())
    mascara.set_name('MaxFactor')
    print(mascara.get_name())
    mascara.enhance()
