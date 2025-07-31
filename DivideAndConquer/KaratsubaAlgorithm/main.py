import KaratsubaAlgorithmAlgo

if __name__ == '__main__':
    while True:
        user_choice = input("\nEnter 'KMultiply' or 'NegativeMultiply' or 'exit' choice : ")
        if user_choice == "KMultiply":
            fnum = int(input("Enter first number : "))
            snum = int(input("Enter second number : "))
            result = KaratsubaAlgorithmAlgo.karatsuba(fnum, snum)
            print(f"Multiplication of {fnum} and {snum} is {result}")
        elif user_choice == "NegativeMultiply":
            fnum = int(input("Enter first number : "))
            snum = int(input("Enter second number : "))
            result = KaratsubaAlgorithmAlgo.karatsuba_Optimized(fnum, snum)
            print(f"Negative Multiplication of {fnum} and {snum} is {result}")
        elif user_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'KMultiply' or 'exit' to stop.")