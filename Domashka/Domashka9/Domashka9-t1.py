class Company:
    """
    Class representing the company Google.
    """

    def __init__(self, name: str, founders: list, year_founded: int, headquarters: str, revenue: float, products: list, employees: int):
        """
        Instance of the class:
        :param name: The name of the company.
        :param founders: A list of the company's founders.
        :param year_founded: The year the company was founded.
        :param headquarters: The location of the company's headquarters.
        :param revenue: The company's annual revenue in billions of dollars.
        :param products: A list of products developed by the company.
        :param employees: The number of employees in the company.
        """

        self._name = name
        self._founders = founders
        self._year_founded = year_founded
        self.headquarters = headquarters
        self.revenue = revenue
        self.products = products
        self._employees = employees

    def show_name(self):
        """
        :return: String with name of the company
        """
        return self._name

    def __str__(self):
        """
        :return: String with general information about company.
        """
        return f"{self._name} is a technology company founded in {self._year_founded} by {', '.join(self._founders)}." \
               f"The main office is located in {self.headquarters}. Company is known by such products, like {', '.join(self.products)}." \
               f"The amount of staff is {self.employees}. Annual revenue of the company is {self.revenue} billions of dollars."

    @property
    def employees(self):
        """
        :return: Number of employees
        """
        return self._employees

    @employees.setter
    def employees(self, value):
        """
        :param value: New amount of employees.
        """
        if value == self._employees:
            return
        if value >= 0:
            self._employees = value
        else:
            raise ValueError("Number of employees cannot be negative")


if __name__ == '__main__':
    google = Company("Google", ["Larry Page", "Sergey Brin"], 1998, "Mountain View, California", 182.53, ["Google Search", "Chrome Browser"], 156000)
    print(google.__str__())
    print(google.show_name())
    print("Number of Employees:", google.employees)
    try:
        google.employees = -100
    except ValueError as e:
        print("Error:", e)
