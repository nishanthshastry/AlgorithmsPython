import ClosestPairofPoints

if __name__ == '__main__':
    while True:
        user_choice = input("\nEnter 'CPP' or 'exit' choice : ")
        if user_choice == "CPP":
            n = int(input("Enter number of points : "))
            points = []
            print("\nEnter each point as two numbers separated by space (e.g., 1 2):")
            for _ in range(n):
                while True:
                    try:
                        x, y = map(float, input(f"Point {_+1}: ").strip().split())
                        points.append((x, y))
                        break
                    except ValueError:
                        print("Invalid input! Please enter two numbers separated by space.")
            print("\nPoints you provided are - ", points)
            closest_distance, closest_pair = ClosestPairofPoints.closest_pair(points)
            print(f"\nThe closest pair of points is: {closest_pair}")
            print(f"\nDistance between them: {closest_distance:.6f}")
        elif user_choice == "exit":
            break
        else:
            print("\nSorry that was an incorrect input - please type 'CPP' or 'exit' to stop.")