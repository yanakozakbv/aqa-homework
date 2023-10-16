from SkinCareProduct import SkinCareProduct


class Lotion(SkinCareProduct):
    """Сlass for Lotion products."""
    def __init__(self, name: str, brand: str, price: float, skin_type: str, scent: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param skin_type: The skin type (oil, dry, normal, combined)
        :param scent: The scent (oud, vanilla etc.)
        """
        super().__init__(name, brand, price, skin_type)
        self.scent = scent

    def soothe(self):
        """Soothes and hydrates the skin."""
        print(f"{self.get_name()} soothes and hydrates {self._skin_type} skin.")

    def nourish(self):
        """Nourishes the skin."""
        print(f"{self.get_name()} nourishes {self._skin_type} skin.")

    def apply(self):
        """Applies the lotion product."""
        print(f"Applying {self._name} with {self.scent} scent to {self._skin_type} skin.")


if __name__ == '__main__':
    lotion = Lotion('Daily Lotion', 'Rituals', 500, 'normal', 'floral')
    lotion.soothe()
    lotion.nourish()
    lotion.apply()
    lotion.remove()
    lotion.get_name()
    lotion.get_skin_type()
