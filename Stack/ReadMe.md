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
## Baseball Game   	
## Valid Parentheses   	
## Implement Stack Using Queues   	
## Implement Queue using Stacks   	  	
## Evaluate Reverse Polish Notation   	
## Generate Parentheses   	
## Asteroid Collision   	
## Daily Temperatures   	
## Online Stock Span   	
## Car Fleet   	
## Simplify Path   	
## Decode String   	
## Maximum Frequency Stack   	
## Largest Rectangle In Histogram
