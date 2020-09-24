array1 = [2, 3, 1, 9, 23, 8, 0, 5]
array2 = [-1, 2, 9, 3, 1, 10, 6, 0]


def bubbleSort(array):
    print("Unsorted: ", array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp


def main():
    bubbleSort(array1)
    print("Sorted: ", array1)
    bubbleSort(array2)
    print("Sorted: ", array2)


main()
