class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


# first method
data_one = Data()
print(f"Значения элементов до изменения:\n{data_one.nums}")
data_one.nums[0] = 100
print(f"Значения элементов после изменения:\n{data_one.nums}")
# 2nd method
data_two = Data()
print(f"Значения элементов до изменения:\n{data_two.nums}")
data_two.change_data(0, 100)
print(f"Значения элементов после изменения:\n{data_two.nums}")
