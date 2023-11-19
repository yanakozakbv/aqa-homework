from interfaces.iwrite import Write


class TxtWriter(Write):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def write(self, text):
        with open(self.__file_path, 'w') as file:
            return file.write(text)
