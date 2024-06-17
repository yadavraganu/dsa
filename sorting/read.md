# Selection Sort
Best and Worst Time: O(n²)  
Space: Constant

![selection_sort.gif](selection_sort.gif)

# Bubble Sort
Average and Worst Case Time: O(n²)  
Best Case Time: O(n)  
Space: 1  

### Algorithm
We assume list is an array of n elements. We further assume that swap function swaps the values of the given array elements.
1. Check if the first element in the input array is greater than the next element in the array. 
2. If it is greater, swap the two elements; otherwise move the pointer forward in the array. 
3. Repeat Step 2 until we reach the end of the array. 
4. Check if the elements are sorted; if not, repeat the same process (Step 1 to Step 3) from the last element of the array to the first. 
5. The final output achieved is the sorted array.

![bubble_sort.gif](bubble_sort.gif)

# Insertion Sort
Best Time: O(n)  
Worst Time: O(n²)  
Space: Constant

### Algorithm
1. We have to start with second element of the array as first element in the array is assumed to be sorted. 
2. Compare second element with the first element and check if the second element is smaller then swap them. 
3. Move to the third element and compare it with the second element, then the first element and swap as necessary to put it in the correct position among the first three elements. 
4. Continue this process, comparing each element with the ones before it and swapping as needed to place it in the correct position among the sorted elements. 
5. Repeat until the entire array is sorted
![insertion_sort.gif](insertion_sort.gif)
