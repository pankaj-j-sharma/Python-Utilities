import random


# Important Features


class MergeSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.merge_sort(self.arr)

    def merge_sort(self,array):
        if len(array)<=1:
            return
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        self.merge_sort(left)
        self.merge_sort(right)

        self.merge_two_sorted_lists(left,right,array)

    def merge_two_sorted_lists(self,list1,list2,array):
        len_list1 = len(list1)
        len_list2 = len(list2)
        i = j = k = 0

        while i < len_list1 and j < len_list2:
            if list1[i] <= list2[j]:
                array[k] = list1[i]
                i+=1
            else:
                array[k] = list2[j]
                j+=1
            k+=1

        while i < len_list1:
            array[k] = list1[i]
            i+=1
            k+=1

        while j < len_list2:
            array[k] = list2[j]
            j+=1
            k+=1


    def get_sorted(self):
        print('unsorted arr', self.arr)
        self.sort()
        print('sorted arr', self.arr)


if __name__ == '__main__':
    arr = random.sample(range(10, 100), 5)
    sort_list = MergeSort(arr)
    sort_list.get_sorted()
