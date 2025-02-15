'''
add_extension()和remove_extensions()用于设置浏览器启动时要加载的插件。可以指定数量不限的插件
根据作者的经验，把插件文件解压到一个独立文件夹，然后把插件路径指向这个文件夹，会比较稳定
'''
from DrissionPage import Chromium,ChromiumOptions

co = ChromiumOptions()

co.add_extension(r'D:\SwitchyOmega')

'''
add_extension() 此方法用于添加一个插件到浏览器
remove_extensions() 此方法用于移除配置对象中保存的所有插件路径。如需移除部分插件，请移除全部后再重新添加需要的插件
'''
