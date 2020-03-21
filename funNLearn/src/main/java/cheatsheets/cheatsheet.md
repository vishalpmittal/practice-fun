# Generic cheetsheet

## Newton formula for square root (sqrt)

``` python
    r = x
    while (r * r > x):
        r = (r + x / r) / 2
    return int(r)
```
