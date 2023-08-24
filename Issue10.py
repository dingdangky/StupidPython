tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm a \\cat."
# unicode编码 \u4e2d\/U00004e00
# Ascii编码 \x41 \141
# \n表示换行
# \r表示回到行的开头，后面的字符会被覆盖
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\u4e2d
\U00004e00
\x41
\141
123\rab
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)