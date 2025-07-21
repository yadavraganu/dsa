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
### Verifying an Alien Dictionary
### Next Permutation
### Remove Duplicates from Sorted Array
### Find First and Last Position of Element in Sorted Array
### Trapping Rain Water
### Median of Two Sorted Arrays
### Valid Anagram
### Top K Frequent Elements
### Group Anagrams
### Valid Sudoku
### Encode and Decode Strings
### Longest Consecutive Sequence
