# 이중 for 문

# normal for문:
a = 2

for b in range(1, 10):
    print("%d x %d = %d" % (a, b, a * b))

# 이중 for 문
print("-" * 30)

for a in range(2, 10):
    for b in range(1, 10):
        print("%d x %d = %d" % (a, b, a * b))
    print("-" * 30)
