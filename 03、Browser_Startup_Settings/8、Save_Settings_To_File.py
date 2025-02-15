from DrissionPage import ChromiumOptions

# save() ini 文件的绝对路径， 传入None保存到当前读取的配置文件
co = ChromiumOptions()
co.save(r'C:\Users\python\Desktop\0210\DrissionPage\03、Browser_Startup_Settings\8、setting.ini')

# save_to_default() 用于保存配置项到固定的默认 ini 文件。默认 ini 文件是指随 DrissionPage 内置的那个
co.save_to_default()