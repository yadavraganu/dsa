## Insert Interval
```python
def insert(intervals, newInterval):
    result = []
    for i in intervals:
        if i[1] < newInterval[0]:
            result.append(i)
        elif newInterval[1] < i[0]:
            result.append(newInterval)
            newInterval = i
        else:
            newInterval[0] = min(newInterval[0], i[0])
            newInterval[1] = max(newInterval[1], i[1])
    result.append(newInterval)
    return result
```
