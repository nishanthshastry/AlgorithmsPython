import MergeSortAlgo

if __name__ == '__main__':
    while True:
        user_choice = input("\nEnter 'Msort' or 'exit' choice : ")
        if user_choice == "Msort":
            n = int(input("Enter number of elements : "))
            array = list(map(int, input("\nEnter array elements : ").strip().split()))[:n]
            print("\nYour Array is - ", array)
            MergeSortAlgo.merge_sort(array, 0, len(array))
            print("\nArray when sorted with 'Merge Sort' is - ", array)
        elif user_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'Msort' or 'exit' to stop.")