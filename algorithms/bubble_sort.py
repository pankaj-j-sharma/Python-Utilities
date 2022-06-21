import random

# Important Features
# Non recursive
# Stable
# In place
# Time Complexity: O(N2)
# Auxiliary Space: O(1)


class BubbleSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        arr_length = len(self.arr)
        # first loop to iterate through all the element
        for i in range(arr_length):
            # second loop to iterate until len - i -1
            for j in range(arr_length-i-1):
                # if left element is greater than right than swap the element
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def get_sorted(self):
        print('unsorted arr', self.arr)
        self.sort()
        print('sorted arr', self.arr)


if __name__ == '__main__':
    arr = random.sample(range(10, 100), 50)
    sort_list = BubbleSort(arr)
    sort_list.get_sorted()
