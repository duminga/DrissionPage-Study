from DrissionPage import Chromium

browser = Chromium()  # 创建浏览器对象
browser.set.retry_times(10)  # 设置整体运行参数
tab = browser.latest_tab  # 获取Tab对象
browser.quit()  # 关闭浏览器