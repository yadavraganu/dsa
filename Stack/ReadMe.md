## Min Stack
```python
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
```
## Minimum Remove to Make Valid Parentheses
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)  # Convert string to a list of characters for mutability
        stack = []  # Stores indices of opening parentheses

        # First Pass: Identify and mark invalid ')'
        for i, char in enumerate(chars):
            if char == '(':
                stack.append(i)  # Push index of '(' onto stack
            elif char == ')':
                if stack:
                    stack.pop()  # Pop if a matching '(' is found
                else:
                    # No matching '(' found for this ')', mark it for removal
                    chars[i] = ''  # Replace with empty string to effectively remove

        # Second Pass: Identify and mark invalid '('
        # Any '(' remaining in the stack are unmatched and thus invalid
        while stack:
            invalid_open_idx = stack.pop()
            chars[invalid_open_idx] = ''  # Mark for removal

        # Join the characters to form the final valid string
        return "".join(chars)
```
## Longest Valid Parentheses
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        # Initialize the stack with -1. This serves as a base for calculations
        # and represents the index before the start of a potential valid substring.
        stack = [-1] 

        for i, char in enumerate(s):
            if char == '(':
                # If it's an opening parenthesis, push its index onto the stack.
                stack.append(i)
            else:  # char == ')'
                # If it's a closing parenthesis, pop the top element from the stack.
                stack.pop()

                # Case 1: Stack becomes empty after popping.
                # This means the current ')' didn't find a matching '('.
                # Push the current index as the new "base" for future calculations.
                if not stack:
                    stack.append(i)
                # Case 2: Stack is not empty after popping.This means we found a valid pair.
                # The length of this valid segment is current_index - stack.top().
                # stack[-1] will be the index of the last unmatched opening parenthesis
                # or the initial -1 base.
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
########################################################################
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        left_count = 0  # Counts opening parentheses
        right_count = 0 # Counts closing parentheses
        n = len(s)

        # Pass 1: Scan from left to right
        # This pass handles cases like "(()" and finds valid substrings where
        # the number of '(' equals the number of ')'.
        for i in range(n):
            if s[i] == '(':
                left_count += 1
            else:  # s[i] == ')'
                right_count += 1

            if left_count == right_count:
                # If counts are equal, we found a perfectly balanced valid substring.
                # Its length is twice the count of either parentheses.
                max_length = max(max_length, 2 * right_count)
            elif right_count > left_count:
                # If more ')' appear than '(', the current segment is invalid.
                # Reset counts to start looking for a new valid substring.
                left_count = 0
                right_count = 0

        # Reset counts for the second pass
        left_count = 0
        right_count = 0

        # Pass 2: Scan from right to left
        # This pass handles cases like "((()" which might be missed by the first pass
        # (e.g., "((()" in first pass: left=3, right=1 -> max_len=0.
        # But scanning right-to-left: ")", then "()", then "(()").
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left_count += 1
            else:  # s[i] == ')'
                right_count += 1

            if left_count == right_count:
                # Similar to the first pass, if counts are equal, update max_length.
                max_length = max(max_length, 2 * left_count) # Or 2 * right_count, they are equal
            elif left_count > right_count:
                # If more '(' appear than ')', the current segment (from right to left) is invalid.
                # Reset counts.
                left_count = 0
                right_count = 0
                
        return max_length
```
## Max Stack
```python
class MaxStack:
    def __init__(self):
        self.num = []  # Main stack
        self.max = []  # Max stack

    def push(self, x: int) -> None:
        max_val = x if not self.max else max(x, self.max[-1])
        self.num.append(x)
        self.max.append(max_val)

    def pop(self) -> int:
        self.max.pop()
        return self.num.pop()

    def top(self) -> int:
        return self.num[-1]

    def peekMax(self) -> int:
        return self.max[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer = []

        # Pop until we find the max
        while self.top() != max_val:
            buffer.append(self.pop())

        # Remove the max
        self.pop()

        # Push back the buffered elements
        while buffer:
            self.push(buffer.pop())

        return max_val
```
## Baseball Game
```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i == "C":
                res.pop()
            elif i == "D":
                res.append(int(res[-1]) * 2)
            elif i == "+":
                print(res)
                res.append(int(res[-2]) + int(res[-1]))
            else:
                res.append(int(i))
        return sum(res)
```
## Valid Parentheses   	
## Implement Stack Using Queues   	
## Implement Queue using Stacks   	  	
## Evaluate Reverse Polish Notation   	
## Generate Parentheses   	
## Asteroid Collision
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:  # Traversing stack one by one
            while (
                stack and i < 0 and stack[-1] > 0
            ):  # Only Enter if there is a stack & astroids are moving towards each other
                if abs(i) > stack[-1]:
                    stack.pop()  # Destroy already existing asteroid in stack
                elif abs(i) < stack[-1]:
                    i = 0  # Destroy currrent asteroid
                else:
                    i = 0  # Destroy currrent asteroid
                    stack.pop()  # Destroy already existing asteroid in stack

            if (
                i != 0
            ):  # Only append if asteroids are not moving towards each other and dont append if current asteroids is destroyed
                stack.append(i)

        return stack
```
## Daily Temperatures
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures): # Iterating Temp one by one
            while stack and temp > stack[-1][1]: # Removing from stack when warmer temp detected continously
                op[stack[-1][0]] = i - stack[-1][0] # Setting output for the top element in stack
                stack.pop() # Removing element for which we found warmer temp
            stack.append((i, temp)) # If current temp is not warmer push on to stack
        return op
```
## Online Stock Span   	
## Car Fleet
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time_taken_till_tgt = []

        for i in range(len(position)):
            time_taken_till_tgt.append((position[i],(target - position[i]) / speed[i]))

        time_taken_till_tgt.sort(reverse=True)

        fleet = 0
        max_time_taken = 0

        for t in time_taken_till_tgt:
            if t[1] > max_time_taken:
                fleet += 1
                max_time_taken = t[1]
        return fleet
```
## Simplify Path   	
## Decode String   	
## Maximum Frequency Stack   	
## Largest Rectangle In Histogram
