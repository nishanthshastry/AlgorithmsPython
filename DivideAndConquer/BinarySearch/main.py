import BinarySearchAlgo

if __name__ == '__main__':
    while True:
        search_choice = input("Enter 'iter' or 'recu' choice in Binary search : ")
        if search_choice == "iter":
            n = int(input("Enter number of elements : "))
            array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
            print("\nYour Array is - ", array)
            print("\nYour Array when sorted is - ", sorted(array))
            ele = int(input("Enter the search number from your array : "))
            result = BinarySearchAlgo.binary_search_iter(array, 0, len(array)-1, ele)
            if result != -1:
                res = f"Element is present and its at position {result} in the sorted array"
                print(res)
            else:
                print("Element is not present in array")
        elif search_choice == "recu":
            n = int(input("Enter number of elements : "))
            array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
            print("\nYour Array is - ", array)
            print("\nYour Array when sorted is - ", sorted(array))
            ele = int(input("Enter the search number from your array : "))
            result = BinarySearchAlgo.binary_search_recur(array, 0, len(array)-1, ele)
            if result != -1:
                res = f"Element is present and its at position {result} in the sorted array"
                print(res)
            else:
                print("Element is not present in array")
        elif search_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'iter' or 'recu' or 'exit' to stop.")