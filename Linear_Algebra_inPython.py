import numpy as np


class Cube:
    def __init__(self):
        self.cube1 = []
        self.cube2 = []

    def value(self, value1, value2):
        self.cube1 = value1
        self.cube2 = value2

    def get_row(self, cube, row):
        return cube[row]

    def get_col(self, cube, col):
        res = []
        for i in range(3):
            res.append(cube[i][col])
        return res

    def cube_multiply_1(self, cube1, cube2):  # method 1 ：dot multiply
        row, col = np.array(self.cube1).shape
        res = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            cube_row_val = self.get_row(cube1, i)
            for j in range(col):
                cube_col_val = self.get_col(cube2, j)
                res_lst = list(map(lambda x, y: x * y, cube_row_val, cube_col_val))  # nice achievement
                res_val = 0
                for k in res_lst:
                    res_val += k
                res[i][j] = res_val
        return res

    def cube_multiply_2(self, cube1, cube2):  # method 2 : column transformation
        row, col = np.array(self.cube1).shape
        cube_res_col = [0, 0, 0]
        cube_res = [[0 for m in range(col)] for n in range(row)]
        for i in range(col):  # get the column value of cube 2
            cube2_col_value = self.get_col(cube2, i)
            cube_res_col = [0, 0, 0]
            for j in range(row):  # get the column value of cube 1
                cube1_col_value = self.get_col(cube1, j)
                cube_res_col_value = list(
                    map(lambda x, y: x * y, [cube2_col_value[j] for q in range(col)], cube1_col_value))
                # print(cube1_col_value)
                # print([cube2_col_value[j] for q in range(col)])
                cube_res_col = list(map(lambda x, y: x + y, cube_res_col, cube_res_col_value))
                # print(cube_res_col)
                # print(cube_res_col)
            else:  # put the column value onto the result
                for k in range(col):
                    cube_res[k][i] = cube_res_col[k]

        return cube_res

    def cube_multiply_3(self, cube1, cube2):  # method 3 : row transformation
        row, col = np.array(self.cube1).shape
        cube_res = [[0 for m in range(row)] for n in range(col)]
        for i in range(row):
            cube1_row_value = self.get_row(cube1, i)
            cube_res_row = [0 for l in range(row)]
            for j in range(row):
                cube2_row_value = self.get_row(cube2, j)
                cube_res_row_value = list(
                    map(lambda x, y: x * y, [cube1_row_value[j] for k in range(row)], cube2_row_value))
                # print(cube_res_row_value)
                cube_res_row = list(map(lambda x, y: x + y, cube_res_row, cube_res_row_value))
                # print(cube_res_row)
            else:
                cube_res[i] = cube_res_row

        return cube_res

    def cube_multiply_4(self, cube1, cube2):  # method 4 : matrix transformation
        row, col = np.array(self.cube1).shape
        cube_res = [[0 for m in range(row)] for n in range(col)]
        for i in range(col):
            cube1_col_value = self.get_col(cube1, i)
            cube2_col_value = self.get_row(cube2, i)
            cube_res_value = np.mat(cube1_col_value).T * np.mat(cube2_col_value)
            cube_res += cube_res_value

        return cube_res


cube_init = Cube()
val_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
val_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

cube_init.value(val_1, val_2)
# print(cube_init.cube1, cube_init.cube2)
print('Dot Multiply Result:')
print(cube_init.cube_multiply_1(cube_init.cube1, cube_init.cube2))
print('Column Transformation Result:')
print(cube_init.cube_multiply_2(cube_init.cube1, cube_init.cube2))
# print(cube_init.get_col(cube_init.cube1,2))
print('Row Transformation Result:')
print(cube_init.cube_multiply_3(cube_init.cube1, cube_init.cube2))
print('Matrix Transformation Result:')
print(cube_init.cube_multiply_4(cube_init.cube1, cube_init.cube2))
