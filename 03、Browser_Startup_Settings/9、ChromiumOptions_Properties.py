from DrissionPage import *
'''
📌 address
该属性为要控制的浏览器地址，格式为 ip:port，默认为'127.0.0.1:9222'。

类型：str

📌 browser_path
该属性返回浏览器可执行文件的路径。

类型：str

📌 user_data_path
该属性返回用户数据文件夹路径。

类型：str

📌 tmp_path
该属性返回临时文件夹路径，可用于保存自动分配的用户文件夹路径。

类型：str

📌 download_path
该属性返回默认下载路径文件路径。

类型：str

📌 user
该属性返回用户配置文件夹名称。

类型：str

📌 load_mode
该属性返回页面加载策略。有'normal'、'eager'、'none'三种

类型：str

📌 timeouts
该属性返回超时设置。包括三种：'base'、'page_load'、'script'。

类型：dict

print(co.timeouts)

输出：

{
    'base': 10,
    'page_load': 30,
    'script': 30
}

📌 retry_times
该属性返回连接失败时的重试次数。

类型：int

📌 retry_interval
该属性返回连接失败时的重试间隔（秒）。

类型：float

📌 proxy
该属性返回代理设置。

类型：str

📌 arguments
该属性以list形式返回浏览器启动参数。

类型：list

📌 extensions
该属性以list形式返回要加载的插件路径。

类型：list

📌 preferences
该属性返回用户首选项配置。

类型：dict

📌 system_user_path
该属性返回是否使用系统按照的浏览器的用户文件夹。

类型：bool

📌 is_existing_only
该属性返回是否仅使用已打开的浏览器。

类型：bool

📌 is_auto_port
该属性返回是否仅使用自动分配端口和用户文件夹路径。

类型：bool

📌 is_headless
该属性返回是否以无头模式启动浏览器。

类型：bool
'''