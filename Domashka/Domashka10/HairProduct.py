from CosmeticProduct import CosmeticProduct


class HairProduct(CosmeticProduct):
    """Сlass for Hair products."""
    def __init__(self, name: str, brand: str, price: float, hair_type: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param hair_type: The hair type (wavy, straight, curly, coily)
        """
        super().__init__(name, brand, price)
        self.hair_type = hair_type

    def nourish(self):
        """Provides nourishment to the hair."""
        print(f"{self._name} nourishes {self.hair_type} hair.")

    def style(self):
        """Assists in creating hairstyles."""
        print(f"{self._name} helps style your {self.hair_type} hair.")

    def apply(self):
        """Applies the product to the hair."""
        print(f"Applying {self.get_name()} on {self.hair_type} hair.")

    def remove(self):
        """Removes the product from the hair."""
        print(f"Removing {self.get_name()} from {self.hair_type} hair.")


if __name__ == '__main__':
    hair_product = HairProduct('Nourish Conditioner', 'Pantine', 1500, 'curly')
    hair_product.nourish()
    hair_product.style()
    hair_product.apply()
    hair_product.remove()
    print(hair_product.get_price())
    hair_product.set_price(2000)
    print(hair_product.get_price())
