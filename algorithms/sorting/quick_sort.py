import random


# Important Features


class QuickSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    def quick_sort(self, start, end):
        if start < end:
            partition_index = self.partition(start, end)
            self.quick_sort(start, partition_index - 1)
            self.quick_sort(partition_index + 1, end)

    def partition(self, start, end):
        pivot_index = start
        pivot = self.arr[pivot_index]

        while start < end:
            while start<len(self.arr) and self.arr[start] <= pivot:
                start += 1
            while self.arr[end] > pivot:
                end -= 1
            if start < end:
                self.arr[start], self.arr[end] = self.arr[end], self.arr[start]

        self.arr[pivot_index], self.arr[end] = self.arr[end], self.arr[pivot_index]

        return end

    def get_sorted(self):
        print('unsorted arr', self.arr)
        self.sort()
        print('sorted arr', self.arr)


if __name__ == '__main__':
    arr = random.sample(range(10, 100), 5)
    sort_list = QuickSort(arr)
    sort_list.get_sorted()
