bookList = [{"date": "2017"},
            {"date": "1963"},
            {"date": "2003"}]


def bubbleSort(list_of_dictionaries):
    print("Unsorted: ", list_of_dictionaries)
    for i in range(len(list_of_dictionaries)):
        for j in range(i + 1, len(list_of_dictionaries)):
            year_i = list_of_dictionaries[i]["date"]
            year_j = list_of_dictionaries[j]["date"]

            if year_i > year_j:
                temp = list_of_dictionaries[i]
                list_of_dictionaries[i] = list_of_dictionaries[j]
                list_of_dictionaries[j] = temp


def main():
    bubbleSort(bookList)
    print("Sorted: ", bookList)


main()
