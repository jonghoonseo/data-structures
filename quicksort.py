def quicksort(list, left, right):
    if left < right:
        pivot_index = partition(list, left, right)
        quicksort(list, left, pivot_index-1)
        quicksort(list, pivot_index+1, right)

def partition(list, left, right):
    low = left
    high = right + 1
    pivot = list[left]
    while True:
        # do increment low index while list[low] is smaller than pivot
        while True:
            low += 1
            if list[low] >= pivot:
                break

        # do decrement high index while list[high] is bigger than pivot
        while True:
            high -= 1
            if list[high] <= pivot:
                break

        # if low index is smaller than high index, swap their element
        if low < high:
            list[low], list[high] = list[high], list[low]
        else:
            break

    # swap pivot value to high element
    list[left], list[high] = list[high], list[left]

    return high

if __name__ == "__main__":
    list = [67, 90, 57, 25, 84, 32, 73, 54]
    print("=== Before ===")
    print(list)

    quicksort(list, 0, len(list)-1)

    print("=== After ===")
    print(list)
