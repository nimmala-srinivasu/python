x = 300


def my_fn():
    global x
    x = 200     # became global
    print(x)


def fn2():
    print(x)


my_fn()
fn2()
print(x)

