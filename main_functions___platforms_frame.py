import tkinter as tk
from tkinter import ttk,messagebox

from 已完成.接单平台汇集.important_parts import show_search_content
from 已完成.接单平台汇集.main_functions____paltforms_content import five_eight_net_work_searching, pu_er_chao_ping_net, \
    guang_xi_zhao_ping_net, fu_jian_net, hu_nan_net, jiang_si_net, gui_zhou_net, china_publish_net, he_bei_net


def search_something():
    def inner_search_something():
        search_input = str(search_input_1.get()).strip()
        if messagebox.askyesno('提示',f'你的输入为:\n{search_input}是否确认搜索?'):
            inner_search_something_root.destroy()
            messagebox.showinfo('提示','正在搜索中......')
            try:
                five_eight_net_work_searching(search_input)  # 58网
            except Exception:
                print('58网错误.....')
                return
            try:
                pu_er_chao_ping_net(search_input)  #普洱人才网
            except Exception:
                print('普洱人才网错误.....')
                return
            # try:
            #     guang_xi_zhao_ping_net(search_input)  #广西招聘
            # except Exception:
            #     print('广西招聘网错误.....')
            #     return
            try:
                fu_jian_net(search_input)  #福建人才网
            except Exception:
                print('福建人才网错误......')
                pass
            try:
                hu_nan_net(search_input)  #湖南人才网
            except Exception:
                print('湖南人才网错误......')
                pass
            try:
                jiang_si_net(search_input)  #江西人才网
            except Exception:
                print('江西人才网错误.....')
                pass
            try:
                gui_zhou_net(search_input)  #贵州人才网
            except Exception:
                print('福建人才网错误......')
                pass
            try:
                china_publish_net(search_input)  #中国公共招聘网
            except Exception:
                print('中国公共招聘网错误.....')
                pass
            try:
                he_bei_net(search_input)   #河北人才网
            except Exception:
                print('河北人才网错误.....')
                pass
            ##############展示搜索内容##############
            show_search_content()
            ##############展示搜索内容##############

        else:
            return

    inner_search_something_root = tk.Tk()
    inner_search_something_root.title('搜索页面')
    inner_search_something_root.geometry('500x200')

    tk.Label(inner_search_something_root,text='输入:').grid(row=1,column=0)

    search_input_1 = tk.Entry(inner_search_something_root)
    search_input_1.default_text = '删除此内容以输入搜索内容....'
    search_input_1.insert(0, search_input_1.default_text)
    # search_input_1.bind('<FocusIn>',click_to_clean_column)
    search_input_1.grid(row=1, column=1,columnspan=20,rowspan=4)

    inner_search_something_button =tk.Button(inner_search_something_root,text='搜索',command=inner_search_something)
    inner_search_something_button.grid(row=6,column=2)

    inner_search_something_root.mainloop()

# search_something()