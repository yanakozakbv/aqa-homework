class CustomIterator:
    """Clas to iterate custom sequence """
    def __init__(self,sequence, start: int, end: int):
        """
        Instance of the class:
        :param sequence: list of the numbers
        :param start: start_index
        :param end: end_index
        """
        self.sequence = sequence
        self.start = start
        self.end = end
        self.current = start
        self.__step = 1

    def __iter__(self):
        """Method that returns an iterator for the given argument"""
        return self

    def __next__(self):
        """Method that returns the next item in an iterator"""
        if self.current + self.__step > self.end + 1:
            self.current = self.end
            raise StopIteration
        else:
            result = self.sequence[self.current]
            self.current += self.__step
            return result


if __name__ == '__main__':
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    start_index = 3
    end_index = 12

    example = CustomIterator(seq, start_index, end_index)

    for i in example:
        print(i)



