# 一、默认配置


# 默认配置下，由 DrissionPage 创建的浏览器，用户文件夹在系统临时文件夹的DrissionPage\userData文件夹内，以端口命名。
#
# 假如用 DrissionPage 默认配置在 9222 端口创建一个浏览器，那么用户数据就存放在
# C:\Users\用户名\AppData\Local\Temp\DrissionPage\userData\9222路径。
#
# 这个用户文件夹不会主动清除，下次再使用 9222 端口时，会继续使用。
#
# 如果使用auto_port()，会存放在系统临时文件夹的DrissionPage\autoPortData文件夹内，以端口命名。
#
# 如C:\Users\用户名\AppData\Local\Temp\DrissionPage\autoPortData\21489。
#
# 这个用户文件夹是临时的，用完会被主动清除。



# 二、自定义位置


# 如果要指定用户文件夹存放位置，可用ChromiumOptions对象的set_tmp_path()方法。
# 也可以保持到 ini 文件，可省略每次设置。
# 如第六节中的使用ini文件实现新增全新浏览器

# 三、单独指定某个用户文件夹
# 指定用户文件夹路径，或使用系统文件夹路径

from DrissionPage import Chromium, ChromiumOptions

co = ChromiumOptions().set_user_data_path(r'D:\tmp')
browser = Chromium(co)


from DrissionPage import Chromium, ChromiumOptions

co = ChromiumOptions().use_system_user_path()
browser = Chromium(co)