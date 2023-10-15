from MakeupProduct import MakeupProduct


class Lipstick(MakeupProduct):
    """Сlass for Lipstick products."""
    def __init__(self, name: str, brand: str, price: float, makeup_type: str, color: str ):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param makeup_type: The make-up type (lashes, lips etc.)
        :param color: The color of the product
        """
        super().__init__(name, brand, price, makeup_type)
        self.color = color


    def apply(self):
        """Applies the lipstick product with the specified color shade."""
        print(f"Applying {self.get_name()} with {self.color} color by {self.get_brand()}.")

    def remove(self):
        """Removes the lipstick product."""
        print(f"Removing {self.get_name()} lipstick.")

    def add_shine(self):
        """Adds a glossy shine to the lipstick."""
        print(f"Adding a glossy shine to {self.get_name()} lipstick.")

    def make_matte(self):
        """Converts the lipstick into a matte finish."""
        print(f"Converting {self.get_name()} into a matte finish lipstick.")


if __name__ == '__main__':
    lipstick = Lipstick('LipHoney', 'Clarins', 400, 'lips', 'coral')
    lipstick.apply()
    lipstick.remove()
    lipstick.add_shine()
    lipstick.last_long()
