def son_palindrom(son):
    return str(son) == str(son)[::-1]

# Test qilish
print(son_palindrom(121))  # True
print(son_palindrom(123))  # False
```

```python
def son_palindrom(son):
    return son == int(str(son)[::-1])

# Test qilish
print(son_palindrom(121))  # True
print(son_palindrom(123))  # False
```

```python
def son_palindrom(son):
    return str(son) == str(son)[::-1] and son >= 0

# Test qilish
print(son_palindrom(121))  # True
print(son_palindrom(-121)) # False
print(son_palindrom(123))  # False
