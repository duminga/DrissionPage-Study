# 导入 ChromiumOptions
from DrissionPage import Chromium, ChromiumOptions

# 创建浏览器配置对象，指定浏览器路径
co = ChromiumOptions().set_browser_path(r'D:\chrome.exe')
# 用该配置创建页面对象
browser = Chromium(addr_or_opts=co)

# 配置对象只有在启动浏览器时生效
# 浏览器创建后再修改这个配置是没有效果的
# 接管已打开的浏览器配置也不会生效


# Created with the specified ini file
from DrissionPage import Chromium, ChromiumOptions

# 创建配置对象时指定要读取的ini文件路径
co = ChromiumOptions(ini_path=r'./config1.ini')
# 使用该配置对象创建页面
browser = Chromium(addr_or_opts=co)