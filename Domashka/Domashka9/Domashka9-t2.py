class Employee:
    """
    Class representing an employee.
    """

    def __init__(self, id: int, name: str, surname: str, department: str, position: str, salary: int, age: int, location: str):
        """
            Instance of the class:
            :param id: The employee's unique identifier.
            :param name: The employee's first name.
            :param surname: The employee's last name.
            :param department: The department to which the employee belongs.
            :param position: The employee's job position.
            :param salary: The employee's salary in the employee's local currency.
            :param age: The employee's age.
            :param location: The employee's current location or office.
        """
        self._id = id
        self._name = name
        self._surname = surname
        self._department = department
        self._position = position
        self._salary = salary
        self.__age = age  # Private attribute
        self._location = location

    def __str__(self):
        """
        :return: String with general information about employee.
        """
        return f"Employee ID: {self._id}\n" \
               f"Full Name: {self.full_name}\n"\
               f"Department: {self._department}\n"\
               f"Position: {self._position}\n"\
               f"Salary: {self._salary}\n"\
               f"Age: {self.__age}\n" \
               f"Location: {self._location}"

    @property
    def id(self) -> int:
        """
        :return: The id of the employee
        """
        return self._id

    @property
    def full_name(self) -> str:
        """
        :return: Name and the surname of the employee
        """
        return f"{self._name} {self._surname}"

    @property
    def salary(self) -> int:
        """
        :return: The salary of the employee
        """
        return self._salary

    @salary.setter
    def salary(self, value: int):
        """
        :param value: The salary amount.
        Setter for salary check.
        """
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative")

    @staticmethod
    def is_adult(employee):
        """
        :param employee
        :return: The False or True, depends on if the employee is adult or not.
        """
        return employee.__age >= 21

    @classmethod
    def change_location(cls, employee, new_location):
        """
        This method changing the location of the employee.
        :param employee: The employee who changing the location.
        :param new_location: New location of the employee.
        """
        employee._location = new_location



if __name__ == '__main__':

    john_doe = Employee(1, "John", "Doe", "IT", "Python Engineer", 7500, 25, "New York")

    print("Employee Information:")
    print(john_doe.__str__())

    print("Is employee is an adult:", Employee.is_adult(john_doe))

    Employee.change_location(john_doe, "San Francisco")

    print("\nUpdated employee  information:")
    print(john_doe.__str__())

    # Attempting to set a negative age will raise an error
    try:
        john_doe.__age = -35
    except ValueError as e:
        print("Error:", e)
