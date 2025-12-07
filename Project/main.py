from bubble_sort import bubble_sort
from quick_sort import quick_sort

def main():
    try:
        nums = input("Enter integers separated by space: ").strip().split()
        nums = [int(x) for x in nums]

        print("Choose sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Quick Sort")
        choice = input("Enter 1 or 2: ").strip()

        if choice == '1':
            sorted_nums = bubble_sort(nums)
        elif choice == '2':
            sorted_nums = quick_sort(nums)
        else:
            print("Invalid choice. Please select 1 or 2.")
            return
        
        print("Sorted numbers:", sorted_nums)
    except ValueError:
        print("Error: Please enter valid integers only.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()