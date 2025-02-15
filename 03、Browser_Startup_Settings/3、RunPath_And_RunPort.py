from DrissionPage import *

# set_browser_path()  此方法用于设置浏览器可执行文件路径
co = ChromiumOptions()
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
ChromiumOptions().set_browser_path(path).save()
page = Chromium(co)

'''
set_tmp_path() 此方法用于设置临时文件默认路径

set_local_port() 此方法用于设置本地启动端口

set_address() 此方法用于设置浏览器地址，格式 'ip:port'

auto_port() 此方法用于设置是否使用自动分配的端口，启动一个全新的浏览器 如：co.auto_port(True)
auto_port()支持多线程，但不支持多进程。
多进程使用时，可用scope参数指定每个进程使用的端口范围，以免发生冲突

set_user_data_path() 此方法用于设置用户文件夹路径。用户文件夹用于存储当前登陆浏览器的账号在使用浏览器时留下的痕迹，包括设置选项等
use_system_user_path() 此方法设置是否使用系统安装的浏览器默认用户文件夹
set_cache_path() 此方法用于设置缓存路径
existing_only() 此方法设置是否仅使用已启动的浏览器，如连接目标浏览器失败，会抛出异常，不会启动新浏览器
'''

