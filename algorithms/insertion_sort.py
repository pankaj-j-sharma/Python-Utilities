import random

# Important Features
# Non-recursive
# Stable
# In place
# O(n²)


class InsertionSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        arr_length = len(self.arr)
        # first loop to iterate through all the element
        for i in range(arr_length):
            # find minimum from the rest unsorted array
            # initialise from the current element
            min_idx = i
            for j in range(i+1, arr_length):
                if self.arr[min_idx] > self.arr[j]:
                    min_idx = j
            # after finding the minimum index swap the elements
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

    def get_sorted(self):
        print('unsorted arr'.ljust(20), self.arr)
        self.sort()
        print('sorted arr'.ljust(20), self.arr)


if __name__ == '__main__':
    arr = random.sample(range(10, 100), 30)
    sort_list = InsertionSort(arr)
    sort_list.get_sorted()
