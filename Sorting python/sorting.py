# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

# inside the folder in terminal
# git add --all
# git commit -m "your message"
# git push

import random


class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []


    def sort_init(self, N):
        """initialize the data structure
        """
        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')

        self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id


    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp


        return self.id

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for i_idx in range (1, len(self.id)):
            min=self.id[i_idx]

            j_idx= i_idx-1

            while j_idx >=0 and min< self.id[j_idx]:
                self.id[j_idx+1]= self.id[j_idx]
                j_idx-= 1
            self.id[j_idx+1]=min
        return self.id


    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """

        N = len(self.id)
        H=N//2

        while H >0:
            for i_idx in range(H,N):
                temp= self.id[i_idx]
                j_idx=i_idx

                while(j_idx >= H and self.id[j_idx-H]> temp):
                    self.id[j_idx]= self.id[j_idx-H]
                    j_idx-=H

                self.id[j_idx]= temp
            H//=2


        return self.id

    def heapify(self, N, i_idx):
        large = i_idx
        left = 2 * i_idx + 1
        right = 2 * i_idx + 2

        if left < N and self.id[i_idx] < self.id[left]:
            large = left

        if right < N and self.id[large] < self.id[right]:
            large = right

        if large != i_idx:
            self.id[i_idx], self.id[large] = self.id[large], self.id[i_idx]
            self.heapify( N, large)




    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """

        N = len(self.id)

        for i in range(N, -1, -1):
            self.heapify( N, i)

        for i in range( N - 1, 0, -1):
            self.id[i], self.id[0] = self.id[0], self.id[i]
            self.heapify( i, 0)

        return self.id



    def mergeLISTS(self, left, right):
        i=0
        j=0
        result=[]

        while(i<len(left) and j <len(right)):
            if left[i] <right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1

        result += left[i:]
        result += right[j:]
        result=self.id
        return result

    def merge(self, list):
        n = len(list)
        if n > 1:
            mid = n // 2
            left = list[:mid]
            right = list[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i = i + 1
                else:
                    list[k] = right[j]
                    j = j + 1
                k = k + 1
            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1
    def mergesort(self,aux):
        self.merge(self.id)

        return self.id


    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        self.mergesort(self.id)


        return self.id


    def partition(self, list, low, high):
        i = (low - 1)
        pind = list[high]

        for j in range(low, high):
            if list[j] <= pind:
                i = i + 1
                list[i], list[j] = list[j], list[i]

        list[i + 1], list[high] = list[high], list[i + 1]

        return i + 1

    def quick(self, arr, lo, hi):
        if lo < hi:
            ind = self.partition(arr, lo, hi)
            self.quick(arr, lo, ind - 1)
            self.quick(arr, ind + 1, hi)
        # return self.id

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """

        self.quick(self.id, 0, len(self.id) - 1)
        return self.id

#this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.

    # Uncomment below to graph results
    #plt.plot(self.id(leng), timing)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.title('log')
    #plt.ylabel('some numbers')
    #plt.show()