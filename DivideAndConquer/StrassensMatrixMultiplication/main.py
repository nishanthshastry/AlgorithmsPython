import StrassensMatrixMultiplicationAlgo

if __name__ == '__main__':
    while True:
        user_choice = input("\nEnter 'SMultiply!' or 'exit' choice : ")
        if user_choice == "SMultiply!":
            try:
                size = int(input("Enter the size of square matrices (e.g., 2, 4, 8): "))
                
                if size <= 0:
                    raise ValueError("Matrix size must be a positive integer.")

                A = StrassensMatrixMultiplicationAlgo.get_matrix_input(size, "A")
                B = StrassensMatrixMultiplicationAlgo.get_matrix_input(size, "B")

                print("\nMatrix A:")
                print(A)
                print("\nMatrix B:")
                print(B)

                result = StrassensMatrixMultiplicationAlgo.strassen_multiply(A, B)

                print("\nResult of Strassen Matrix Multiplication:")
                print(result)

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif user_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'SMultiply!' or 'exit' to stop.")