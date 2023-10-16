from SkinCareProduct import SkinCareProduct


class Tonik(SkinCareProduct):
    """Сlass for Tonik products."""
    def __init__(self, name: str, brand: str, price: float, skin_type: str, action: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param skin_type: The skin type (oil, dry, normal, combined)
        :param action: The action of the tonik (exfoliating, calming, clearing)
        """

        super().__init__(name, brand, price, skin_type)
        self._action = action

    def balance_ph(self):
        """Balances the skin's pH level."""
        print(f"{self.get_name()} balances the pH level of {self._skin_type} skin.")

    def perform_action(self):
        """Performs the specific action of the tonic."""
        print(f"{self.get_name()} {self._action} {self._skin_type} skin.")

if __name__ == '__main__':
    tonik = Tonik('Calming Toner', 'Obadji', 1500, 'dry', 'calming')
    tonik.balance_ph()
    tonik.perform_action()
    tonik.apply()
    tonik.hydrate()
