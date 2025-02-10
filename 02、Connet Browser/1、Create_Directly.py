from DrissionPage import Chromium

# browser = Chromium()
# 默认方式:直接创建，这种方式代码最简洁，程序会使用默认配置，自动生成页面对象

# 接管9333端口的浏览器，如该端口空闲，启动一个浏览器
browser = Chromium(9333)
browser = Chromium('127.0.0.1:9333')
# 指定端口或地址：创建Chromium对象时向addr_or_opts参数传入端口号或地址，可接管指定端口浏览器，若端口空闲，使用默认配置在该端口启动一个浏览器。