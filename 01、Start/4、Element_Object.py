from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get('https://DrissionPage.cn')
ele = tab.ele('text=文档')  # 获取文本为“文档”的元素
# 元素对象ChromiumElemet是交互的执行者，如点击、文本输入、获取元素信息等。
ele.click()  # 点击该元素