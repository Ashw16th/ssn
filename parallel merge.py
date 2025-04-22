import concurrent.futures

class ParallelMergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def parallel_merge_sort(self):
        if len(self.arr) <= 1:
            return self.arr
        
        mid = len(self.arr) // 2
        with concurrent.futures.ThreadPoolExecutor() as executor:
            left_future = executor.submit(self.parallel_merge_sort_helper, self.arr[:mid])
            right_future = executor.submit(self.parallel_merge_sort_helper, self.arr[mid:])
            
            left = left_future.result()
            right = right_future.result()

        return self.merge(left, right)

    def parallel_merge_sort_helper(self, arr):
        """ Helper method for parallelism in merge sort """
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.parallel_merge_sort_helper(arr[:mid])
        right = self.parallel_merge_sort_helper(arr[mid:])
        return self.merge(left, right)

# Taking user input
def user_input():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        arr.append(num)
    
    sorter = ParallelMergeSort(arr)
    sorted_arr = sorter.parallel_merge_sort()
    print(f"\nSorted Array: {sorted_arr}")

# Example usage
if __name__ == "__main__":
    user_input()
