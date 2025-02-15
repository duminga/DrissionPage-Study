from DrissionPage import *
'''
除了启动参数，还有大量配置信息保存在浏览器的 preferences 文件中
preferences 文件是Chromium内核浏览器的配置信息文件，与 DrissionPage 的 configs.ini 完全不同
'''

# set_user() Chromium 浏览器支持多用户配置，我们可以选择使用哪一个。默认为'Default'
co = ChromiumOptions()
co.set_user(user='xing')
# 如这样可以设置用户配置文件夹名称
page = Chromium(co)


# set_pref() 此方法用于设置用户配置文件里的一个配置项
# 禁止所有弹出窗口
co.set_pref(arg='profile.default_content_settings.popups', value='0')
# 隐藏是否保存密码的提示
co.set_pref('credentials_enable_service', False)


# remove_pref() 此方法用于在当前配置对象中删除一个pref配置项
co.remove_pref(arg='profile.default_content_settings.popups')


# remove_pref_from_file() 此方法用于在用户配置文件删除一个配置项。注意与上一个方法不一样，如果用户配置文件中已经存在某个项
# 用remove_pref() 是不能删除的，只能用remove_pref_from_file()删除
co.remove_pref_from_file(arg='profile.default_content_settings.popups')


# clear_prefs() 方法用于清空已设置的prefs参数