import QuickSortAlgo

if __name__ == '__main__':
    while True:
        user_choice = input("\nEnter 'Qsort' or 'exit' choice : ")
        if user_choice == "Qsort":
            n = int(input("Enter number of elements : "))
            array = list(map(int, input("\nEnter array elements : ").strip().split()))[:n]
            print("\nYour Array is - ", array)
            QuickSortAlgo.quick_sort(array, 0, len(array) - 1)
            print("\nArray when sorted with 'Quick Sort' is - ", array)
        elif user_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'Qsort' or 'exit' to stop.")