### Two Sum
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}  # Stores value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [] # Should not reach here based on problem constraints
```
### Best Time to Buy and Sell Stock
```python
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```
### Contains Duplicate
```python
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
```
### Contains Duplicate II
```python
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    num_indices = {}  # Stores value -> last_seen_index
    for i, num in enumerate(nums):
        if num in num_indices and abs(i - num_indices[num]) <= k:
            return True
        num_indices[num] = i
    return False
```
### Product of Array Except Self
```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Calculate prefix products
    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]

    # Calculate suffix products and multiply with prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]

    return answer
```
### Maximum Subarray
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res
```
### Maximum Product Subarray
### Find Minimum in Rotated Sorted Array
### Search in Rotated Sorted Array
### Two Sum II
### 3 Sum
### Merge Sorted Array
### Container With Most Water
```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Calculate current area
        current_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_water)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```
### Verifying an Alien Dictionary
### Next Permutation
### Remove Duplicates from Sorted Array
```python
def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # Pointer for the last unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1  # Length of array with unique elements
```
### Find First and Last Position of Element in Sorted Array
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums,target):
            l,r = 0,len(nums)-1
            first = -1
            while l<=r:
                mid = l + ((r-l)//2)
                if nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                else:
                    r = mid-1
                    first = mid
            return first 
        def binary_search_right(nums,target):
            l,r = 0,len(nums)-1
            last = -1
            while l<=r:
                mid = l + ((r-l)//2)
                if nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
                    last = mid
            return last  
        return  [binary_search_left(nums,target),binary_search_right(nums,target)]
```
### Trapping Rain Water
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])

        return water
```
### Median of Two Sorted Arrays
### Valid Anagram
### Top K Frequent Elements
### Group Anagrams
### Valid Sudoku
### Encode and Decode Strings
### Longest Consecutive Sequence
```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest
```
