from DrissionPage import *
'''
get_tab()
此方法用于获取一个标签页对象或它的 id。

id_or_num不为None时，获取id_or_num指定的标签页。后面几个参数无效。

id_or_num为None时，根据后面几个参数指定的条件查找标签页（与关系）

'''
browser = Chromium()
tab = browser.get_tab()
print(tab)