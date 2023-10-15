from abc import ABC, abstractmethod


class CosmeticProduct:
    """Base class for cosmetic products."""
    def __init__(self, name: str, brand: str, price: float):
        """
        Instance of the class:
        :param name: The name of the product
        :param brand: The brand of the product
        :param price: The price of the product
        """
        self._name = name
        self._brand = brand
        self._price = price

    @abstractmethod
    def apply(self):
        """Abstract method for applying the product."""
        pass

    @abstractmethod
    def remove(self):
        """Abstract method for removing the product."""
        pass

    def get_name(self):
        """Get the name of the product."""
        return self._name

    def get_brand(self):
        """Get the brand of the product."""
        return self._brand

    def get_price(self):
        """Get the price of the product."""
        return self._price

    def set_name(self, name):
        """Set name of the product."""
        self._name = name

    def set_brand(self, brand):
        """Set brand of the product."""
        self._brand = brand

    def set_price(self, price):
        """Set price of the product."""
        self._price = price


    def apply(self):
        """Applies the product to the skin."""
        print(f"Applying {self._name} by {self._brand}.")

    def remove(self):
        """Removes the product from the skin."""
        print(f"Removing {self._name} by {self._brand}.")

if __name__ == '__main__':
    cosmetic = CosmeticProduct('Shower Gel', 'Rituals', 900)
    print(cosmetic.get_brand())
    print(cosmetic.get_price())
    cosmetic.apply()
    cosmetic.remove()
    cosmetic.set_brand('Rituals Inc.')
    print(cosmetic.get_brand())
