class FromTxtToHtml:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        header = lines[0].replace('\n', '').split(',')
        users_data = [user.replace('\n', '').split(',') for user in lines[1:]]
        result = []
        for user in users_data:
            result.extend([f'<{key}>{value}</{key}>' for key, value in zip(header, user)])
        return result

    def print_html(self):
        html_lines = self.txt_to_html()
        for line in html_lines:
            print(line)


if __name__ == '__main__':
    test = FromTxtToHtml('structure.txt').print_html()
