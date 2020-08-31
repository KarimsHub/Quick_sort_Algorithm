import random
import time


def random_numbers_generator():
    l = []
    for i in range(999):
        l.append(random.randint(0,999))
    return l

unsorted_l = random_numbers_generator()
#print(unsorted_l)
start = time.time()

def part(list, low, high):
    pivot = list[high] # defining the pivot element as the last one in the list
    low_cache = low
    high_cache = high

    while low < high:
        while high > low_cache and list[high] >= pivot: # if we find and element which is smaller than the actual pivot element we have to switch both elements
            high = high - 1
        while low <= high_cache and list[low] < pivot:
            low = low + 1
        if low < high:
            list[low], list[high] = list[high], list[low]
        else:
            break

    if list[low] > pivot:
        list[high_cache], list[low] = list[low], list[high_cache]
    return low

def quick_sort(unsorted_list, low = 0, high = None):
    if high is None:
        high = len(unsorted_list) - 1
    if low < high: # want to run the algo until low is higher than high
        pivot = part(unsorted_list, low, high) # gives us the index which will split the list
        quick_sort(unsorted_list, low, pivot - 1) # using the quick sort function on the left side of the unsorted list
        quick_sort(unsorted_list, pivot + 1, high) # using the quick sort function on the right side of the unsorted list


quick_sort(unsorted_l)
print(unsorted_l)
end = time.time()
print(end - start) # checks the amount of time the algorithm needs to sort the list

