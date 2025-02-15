# 页面对象运行时需要用到的参数，也可以在ChromiumOptions中设置
from DrissionPage import *
co = ChromiumOptions()
#一、 set_timeouts() 此方法用于设置几种超时时间，单位为秒。
co.set_timeouts(base=10) # 默认超时时间，用于元素等待、alert 等待、WebPage的 s 模式连接等等，除以下两个参数的场景，都使用这个设置
co.set_timeouts(page_load=10)# 页面加载超时时间
co.set_timeouts(script=10)# JavaScript 运行超时时间

# set_retry() 此方法用于设置页面连接超时时的重试次数和间隔
co.set_retry() #times=int 重连次数  interval=float 重试间隔(秒)


#二、 set_load_mode() 此方法用于设置网页加载策略
'''
加载策略是指强制页面停止加载的时机，如加载完 DOM 即停止，不加载图片资源等，以提高自动化效率。

无论设置哪种策略，加载时间都不会超过set_timeouts()中page_load参数设置的时间。

加载策略：

'normal'：阻塞进程，等待所有资源下载完成（默认）

'eager'：DOM 就绪即停止加载

'none'：网页连接成功即停止加载
'''
co.set_load_mode('eager')
co.set_load_mode('normal')
co.set_load_mode('none')


# 三、set_proxy() 用于设置浏览器代理
'''
格式：协议://ip:port,当不指定协议时，默认使用 http 代理
'''
co.set_proxy('http://127.0.0.1:7890')


# 四、set_download_path() 此方法用于设置下载文件保存路径
co.set_download_path(r'C:\Users\python\Desktop\0210')