# 一、和第四节中多浏览器共存一样用auto_port()
from DrissionPage import Chromium, ChromiumOptions


co = ChromiumOptions().auto_port()

tab1 = Chromium(addr_or_opts=co).latest_tab
tab2 = Chromium(addr_or_opts=co).latest_tab

tab1.get('http://www.baidu.com')
tab2.get('http://www.bing.com')

# 二、使用ChromiumOptions对象的new_env()方法，可指定启动全新的浏览器
# 如果指定端口已有浏览器，会自动关闭再启动新的


co = ChromiumOptions().new_env()
browser = Chromium(co)

# 三、也和第四节中多浏览器共存一样，手动指定一个新的空闲端口避开默认端口即可打开新的浏览器

browser1 = Chromium()
co = ChromiumOptions().set_local_port(9333).set_user_data_path(r'C:\Users\python\Desktop\0210\DrissionPage\02、Connet Browser\No6resourcedata')
browser2 = Chromium(co)