# shell创建新文件有多种方式
# 1. cat > filename 然后输入内容，ctrl+d结束
# 2. touch filename 修改文件时间戳
# 3. echo "content" > filename 输出内容到文件
# 4. vim filename 打开文件编辑

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {0}, arg2: {1}".format(arg1, arg2))
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothing.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()