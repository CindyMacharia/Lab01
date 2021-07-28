a = stdarray.createID(10, 0)
for i in range (10):
    a[i] = a[a[i]]
for v in a:
    stdio.writeIn(v)