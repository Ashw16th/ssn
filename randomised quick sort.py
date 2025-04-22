import random

class RandomizedQuickSort:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, low, high):
        pivot_index = random.randint(low, high)
        self.arr[pivot_index], self.arr[high] = self.arr[high], self.arr[pivot_index]  # Swap pivot with last element
        pivot = self.arr[high]
        
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def randomized_quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.randomized_quick_sort(low, pi - 1)
            self.randomized_quick_sort(pi + 1, high)

    def sort(self):
        self.randomized_quick_sort(0, len(self.arr) - 1)
        return self.arr

# Taking user input
def user_input():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    sorter = RandomizedQuickSort(arr)
    sorted_arr = sorter.sort()
    print("Randomized Quick Sort:", sorted_arr)

# Example usage
if __name__ == "__main__":
    user_input()
