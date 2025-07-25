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
## Largest Rectangle in Histogram
## Minimum Remove to Make Valid Parentheses
## Longest Valid Parentheses
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
## Simplify Path   	
## Decode String   	
## Maximum Frequency Stack   	
## Largest Rectangle In Histogram
