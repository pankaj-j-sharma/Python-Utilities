import random

# Important Features


class ShellSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        array = self.arr 
        size = len(array)
        gap = size//2

        while gap >0:
            for i in range(gap,size):
                anchor = array[i]
                j = i
                while j>=gap and array[j-gap]>anchor:
                    array[j]=array[j-gap]
                    j-=gap
                array[j] = anchor
            gap = gap//2

    def get_sorted(self):
        print('unsorted arr', self.arr)
        self.sort()
        print('sorted arr', self.arr)


if __name__ == '__main__':
    arr = random.sample(range(10, 100), 5)
    sort_list = ShellSort(arr)
    sort_list.get_sorted()
