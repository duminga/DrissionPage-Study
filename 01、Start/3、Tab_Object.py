from DrissionPage import Chromium

browser = Chromium()
tab1 = browser.latest_tab  # 获取最后激活的标签页对象
tab1.get('https://DrissionPage.cn')  # 标签页访问一个网址
tab2 = browser.new_tab('https://www.baidu.com')  # 新建一个标签页并访问网址
tab3 = browser.get_tab(title='DrissionPage')  # 按条件获取标签页对象
# 默认情况下每个标签页只有一个 Tab 对象，关闭单例模式后可用多个 Tab 对象同时控制一个标签页。
print(tab1)
print(tab2)
print(tab3)