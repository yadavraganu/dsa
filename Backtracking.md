## Subsets
```python
def subsets(nums):
    result = []
    n = len(nums)

    def backtrack(index, current_subset):
        result.append(list(current_subset))

        for i in range(index, n):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result
```
## Permutations
```python
```
## Subsets II
```python
```
## Letter Combinations of a Phone Number
```python
```
## Combination Sum
```python
```
## Combination Sum II
```python
```
## Word Search
```python
```
## Word Search II
```python
```
## Palindrome Partitioning
```python
```
## N Queens
```python
```
