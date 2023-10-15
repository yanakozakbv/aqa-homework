from CosmeticProduct import CosmeticProduct


class MakeupProduct(CosmeticProduct):
    """Сlass for Makeup products."""
    def __init__(self, name: str, brand: str, price: float, makeup_type: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param makeup_type: The make-up type (lashes, lips etc.)
        """
        super().__init__(name, brand, price)
        self.makeup_type = makeup_type

    def enhance(self):
        """Enhances the specified makeup look."""
        print(f"{self._name} enhances {self.makeup_type} look.")

    def last_long(self):
        """Helps makeup last longer."""
        print(f"{self._name} makes your {self.makeup_type} last longer.")


if __name__ == '__main__':
    makeup_product = MakeupProduct('Les Beiges', 'Chanel', 1700, 'lips')
    makeup_product.enhance()
    makeup_product. last_long()
    makeup_product.apply()
    makeup_product.remove()
    print(f'The price of {makeup_product.get_name()} is {makeup_product.get_price()}')