__author__ = "Bilal El Uneis"
__since__ = "August 2018"
__email__ = "bilaleluneis@gmail.com"


class Matrix:

    def __init__(self, rows: int, columns: int, values: [int]):
        if (rows * columns) != len(values):
            raise Exception("Matrix cannot be instantiated due to mismatch of input to rows * columns!! WTF!!")
        self.__rows = rows
        self.__columns = columns
        self.__matrix = values[:]  # returns a copy of values

    @property
    def data(self) -> [int]:
        return self.__matrix

    @property
    def num_of_rows(self) -> int:
        return self.__rows

    @property
    def num_of_columns(self) -> int:
        return self.__columns

    @property
    def size(self) -> int:
        return len(self.__matrix)

    def __str__(self):
        index = 0
        matrix_as_string = "\n"
        for _ in range(0, self.num_of_rows):
            matrix_as_string += "|"
            for _ in range(0, self.num_of_columns):
                if index >= self.size:
                    break
                matrix_as_string += " {} ".format(self.__matrix[index])
                index += 1
            matrix_as_string += "|\n"
        return matrix_as_string

    @staticmethod
    def pretty_print(m1: 'Matrix', m2: 'Matrix', m3: 'Matrix', operation: str = "*") -> str:
        # quick and dirty way to get the max size of rows and columns to loop through
        max_rows = sorted([m1.num_of_rows, m2.num_of_rows, m3.num_of_rows])[2]
        # max_columns = sorted([m1.num_of_columns, m2.num_of_columns, m3.num_of_columns])[2]
        result = ""
        for index in range(0, max_rows):
            result += Matrix.__get_row(m1, index) + \
                      Matrix.__get_row(m2, index) + \
                      Matrix.__get_row(m3, index) + "\n"
        return result

    @staticmethod
    def __get_row(matrix: 'Matrix', at_index: int) -> str:
        if at_index >= matrix.num_of_rows:
            return ""
        start_index: int = 0
        if at_index != 0:
            start_index = at_index + matrix.num_of_columns
        row = ""
        for index in range(start_index, matrix.num_of_columns):
            row += " {} ".format(matrix.data[index])
        return row


def main():
    matrix = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    matrix2 = Matrix(2, 2, [5, 6, 7, 8])
    matrix3 = Matrix(4, 2, [9, 8, 0, 6, 7, 8, 0, 6])
    print(matrix)
    result = Matrix.pretty_print(matrix, matrix2, matrix3)
    print(result)


# start of running code
if __name__ == "__main__":
    main()
