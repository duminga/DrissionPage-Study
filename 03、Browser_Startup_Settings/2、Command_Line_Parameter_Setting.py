from DrissionPage import  Chromium, ChromiumOptions
# Chromium 内核浏览器有一系列的启动配置，以--开头，可在浏览器创建时传入，控制浏览器行为和初始状态


co = ChromiumOptions()


# 一、set_argument()  此方法用于设置启动参数
# 设置启动时最大化
# co.set_argument('--start-maximized')
# # 设置初始窗口大小
# co.set_argument('--window-size', '800,600')
# 使用来宾模式打开浏览器
co.set_argument('--guest')



# 二、remove_argument()  此方法用于在启动配置中删除一个启动参数，只要传入参数名称即可，不需要传入值

# 删除--start-maximized参数
co.remove_argument('--start-maximized')
# 删除--window-size参数
co.remove_argument('--window-size')


# 三、clear_arguments()   此方法用于清空已设置的arguments参数。

co.clear_arguments()

# co.set_argument('--start-maximized')




page = Chromium(co)