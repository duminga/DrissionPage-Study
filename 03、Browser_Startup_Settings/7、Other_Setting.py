from DrissionPage import *
'''
一、headless()
该方法用于设置是否以无界面模式启动浏览器。

如果指定端口已存在运行中的非无头浏览器，会先关闭已有浏览器再启动新的。
on_off	bool	True	True和False表示开或关
'''
co = ChromiumOptions()
co.headless(True)


'''
二、new_env()
该方法用于设置是否使用全新环境创建浏览器。

如果指定端口已存在运行中的浏览器，会先关闭已有浏览器再启动新的
on_off	bool	True	True和False表示开或关
'''
co.new_env()


'''
三、set_flag()
此方法用于设置实验项，即'chrome://flags'中的项目。

设置无值的项，无须设置value参数，否则在该参数传入要设置的值。

flag	str	必填	设置项名称
value	str	None	设置项值
'''

co.set_flag('temporary-unexpire-flags-m118', '1')  # 有值
co.set_flag('disable-accelerated-2d-canvas')  # 无值


'''
其他：
clear_flags_in_file() 此方法用于删除浏览器配置文件中已设置的实验项
clear_flags() 此方法用于清空本对象中已设置的flags参数
incognito() 该方法用于设置是否以无痕模式启动浏览器
ignore_certificate_errors() 该方法用于设置是否忽略证书错误。可以解决访问网页时出现的“您的连接不是私密连接”、“你的连接不是专用连接”等问题
no_imgs() 该方法用于设置是否禁止加载图片
no_js() 该方法用于设置是否禁用 JavaScript
mute() 静音
set_user_agent() 该方法用于设置 user agent
set_paths() 
此方法用于设置各种路径信息。对有传入值的路径进行设置，为None的则无视。
方法的功能与上面介绍过设置路径的方法是重复的，只是把几个方法集成在一起。
参数名称	类型	默认值	说明
browser_path	str
                Path	None	浏览器可执行文件路径
local_port	str
            int	None	浏览器要使用的本地端口号
address	str	None	浏览器地址，例：127.0.0.1:9222，如与local_port一起设置，会覆盖local_port的值
download_path	str
                Path	None	下载文件默认保存路径
user_data_path	str
                Path	None	用户数据文件夹路径
cache_path	str
            Path	None	缓存路径
co.set_paths(local_port=9333, user_data_path=r'D:\tmp')
'''