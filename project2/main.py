def counter():
    n = 0

    def incr():
        nonlocal n
        x = n
        n += 1
        return x

    return incr


c = counter()
print(c())
print(c())
print(c())
print(c.__closure__[0].cell_contents)  # 查看闭包的元素