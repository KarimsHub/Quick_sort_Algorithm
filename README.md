# Quick sort Algorithm

Quick sort is a highly efficient divide and conquer sorting algorithm and is based on partitioning of array of data into smaller arrays


## Working of this algorithm:
-  It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.


## Complexity:
- Quick sort has an best case of O(n log(n)), average of O(n log(n))and worst-case of O(n²)

## Advantages of Quick sort:

- Quick sort is an in-place sorting algorithm. In-place sorting means no additional storage space is needed to perform sorting.
- The worst case of quicksort O(n2) can be avoided by using randomized quicksort. It can be easily avoided with high probability by choosing the right pivot.
- Quicksort in particular exhibits good cache locality and this makes it faster than merge sort in many cases like in virtual memory environment.

## Disadvantages of Quick sort:

- its worst-case performance is similar to average performances of the bubble, insertion or selections sorts
- Unstable


![ImgName](https://github.com/KarimsHub/Quick_sort_Algorithm/blob/master/partitionA.png?raw=true)
