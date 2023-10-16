from CosmeticProduct import CosmeticProduct


class SkinCareProduct(CosmeticProduct):
    """Сlass for SkinCare products."""
    def __init__(self, name: str, brand: str, price: float, skin_type: str):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        :param skin_type: The skin type (oil, dry, normal, combined)
        """
        super().__init__(name, brand, price)
        self._skin_type = skin_type

    def get_skin_type(self):
        """Get the skin type."""
        return self._skin_type

    def hydrate(self):
        """Provides hydration to the skin."""
        print(f"{self.get_name()} hydrates {self._skin_type} skin.")

    def protect(self):
        """Protects the skin from UV rays."""
        print(f"{self.get_name()} protects {self._skin_type} skin from UV rays.")

    def apply(self):
        """Applies the product to the skin."""
        print(f"Applying {self.get_name()} on {self._skin_type} skin.")

    def remove(self):
        """Removes the product from the skin."""
        print(f"Removing {self.get_name()} from {self._skin_type} skin.")


if __name__ == '__main__':
    skin_product = SkinCareProduct('Renewal Cream', 'Obadji', 4000, 'oil')
    skin_product.hydrate()
    skin_product.protect()
    skin_product.apply()
    skin_product.remove()
    f'The brand of {skin_product.get_name()} is {skin_product.get_brand()}'

    skin_product2 = SkinCareProduct('Clearing foam', 'Medic8', 3500, 'normal')
    skin_product2.hydrate()
    skin_product2.protect()
    skin_product2.apply()
    skin_product2.remove()
    f'The brand of {skin_product2.get_name()} is {skin_product2.get_brand()}'
