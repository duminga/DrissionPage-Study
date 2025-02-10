# 创建配置对象后，可调整配置内容，然后在页面对象创建时以参数形式把配置对象传递进去，页面对象会根据配置对象的内容对浏览器进行初始化
from DrissionPage import Chromium, ChromiumOptions

# 创建配置对象（默认从 ini 文件中读取配置）
co = ChromiumOptions()
# 设置不加载图片、静音
co.no_imgs(True).mute(True)

# 以该配置创建页面对象
page = Chromium(addr_or_opts=co)


co = ChromiumOptions()
co.incognito()  # 匿名模式
co.headless()  # 无头模式
co.set_argument('--no-sandbox')  # 无沙盒模式
page = Chromium(co)