from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get('https://DrissionPage.cn')
ele1 = tab.ele('text=文档')  # 获取文本为“文档”的元素
ele2 = ele1.next()  # 获取ele1的后一个元素
ele2.click()  # 点击该元素