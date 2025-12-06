def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    try:
        nums = input("Enter integers separated by space: ").strip().split()
        nums = [int(x) for x in nums]
        sorted_nums = bubble_sort(nums)
        print("Sorted numbers:", sorted_nums)
    except ValueError:
        print("Error: Please enter valid integers only.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()