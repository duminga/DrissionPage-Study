from DrissionPage import ChromiumOptions,Chromium
co = ChromiumOptions()
page = Chromium(co)


# new_tab(),有四个参数:url、new_window、background、new_context
page.new_tab('https://www.baidu.com',new_window=True)


# activate_tab(),此方法用于使一个标签页显示到前端。可传入 Tab 对象、标签页 id、标签页序号
page.activate_tab()


# close_tabs(),用于关闭标签页。可指定多个，可关闭指定标签页以外的
page.close_tabs()