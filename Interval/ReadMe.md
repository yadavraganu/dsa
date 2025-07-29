## Insert Interval
```python
def insert(intervals, newInterval):
    result = []
    for i in intervals:
        # If current interval ends before newInterval starts, add it directly
        if i[1] < newInterval[0]:
            result.append(i)
        # If newInterval ends before current interval starts, insert newInterval and update it
        elif newInterval[1] < i[0]:
            result.append(newInterval)
            newInterval = i
        else:
            # Overlapping intervals, merge them
            newInterval[0] = min(newInterval[0], i[0])
            newInterval[1] = max(newInterval[1], i[1])
    result.append(newInterval)
    return result
```
