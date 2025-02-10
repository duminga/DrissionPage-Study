# 初始默认配置下，程序会为每个使用的端口创建空的用户目录，并且每次接管都使用，这样可以有效避免浏览器冲突。
# 有些时候我们希望使用系统安装的浏览器的默认用户文件夹。以便复用用户信息和插件等

from DrissionPage import Chromium, ChromiumOptions

co = ChromiumOptions().use_system_user_path()
browser = Chromium(co)

# 和设置多浏览器共存一样，同样可以save()在int文件保存设置
# ChromiumOptions().use_system_user_path().save()