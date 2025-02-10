# 导入 ChromiumOptions
from DrissionPage import Chromium, ChromiumOptions

# 创建浏览器配置对象，指定浏览器路径
co = ChromiumOptions().set_browser_path(r'D:\chrome.exe')
# 用该配置创建页面对象
browser = Chromium(addr_or_opts=co)