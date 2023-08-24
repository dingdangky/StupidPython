from sys import argv
# argv是脚本参数输入，在python3运行命令时就需要输入；
# input是在程序执行过程中需要输入
script,first,second,third=argv
print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
