
# 一、指定独立端口和数据文件夹
from DrissionPage import Chromium, ChromiumOptions

# 如果想要同时操作多个浏览器，或者自己在使用其中一个上网，同时控制另外几个跑自动化，
# 就需要给这些被程序控制的浏览器设置单独的 端口 和 用户文件夹，否则会造成冲突。

# 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
co1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'C:\Users\python\Desktop\0210\DrissionPage\02、Connet Browser\No4resourcedata1')
co2 = ChromiumOptions().set_paths(local_port=9222, user_data_path=r'C:\Users\python\Desktop\0210\DrissionPage\02、Connet Browser\No4resourcedata2')

# 创建多个页面对象
tab1 = Chromium(addr_or_opts=co1).latest_tab
tab2 = Chromium(addr_or_opts=co2).latest_tab

# 每个页面对象控制一个浏览器
tab1.get('https://DrissionPage.cn')
tab2.get('https://www.baidu.com')


# 每个浏览器都要设置独立的端口号和用户文件夹，二者缺一不可。



# 二、auto_port()方法

# ChromiumOptions对象的auto_port()方法，可以指定程序每次使用空闲的端口和临时用户文件夹创建浏览器

# 使用auto_port()的配置对象可由多个Chromium对象共用，不会出现冲突

# 这种方式创建的浏览器是全新不带任何数据的，并且运行数据会自动清除


co = ChromiumOptions().auto_port()

tab3 = Chromium(addr_or_opts=co).latest_tab
tab4 = Chromium(addr_or_opts=co).latest_tab

tab3.get('https://DrissionPage.cn')
tab4.get('https://www.baidu.com')

# 三、在 ini 文件设置自动分配
# 可以把自动分配的配置记录到 ini 文件，这样无需创建ChromiumOptions
# 每次启动的浏览器都是独立的，不会冲突。但和auto_port()一样，这些浏览器也不能复用

# ChromiumOptions().auto_port(True).save()