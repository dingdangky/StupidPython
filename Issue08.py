formatter = "{} {} {} {}"

# 根本原因是"{}"既是一个字符串，也是一个格式化符号。
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(formatter.format(1, 2, 3, 4), formatter.format(1, 2, 3, 4), formatter.format(1, 2, 3, 4),formatter.format(1, 2, 3, 4)))
print(formatter.format("Try your","Own text here","Maybe a poem","Or a song about fear"))