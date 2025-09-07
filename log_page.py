import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import json

from 已完成.接单平台汇集.main_functions___frame import progress_to_search


def encryption(some):
    the_head = 'qwerty'
    the_tail = '!??!!'
    final = '{}{}{}'.format(the_head, some, the_tail)
    return hashlib.md5(final.encode('utf-8')).hexdigest()


def click_to_clean_column(event):
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

def point_out_of_window(event):
    if event.widget.get() == '':
        event.widget.insert(0, event.widget.default_text)
        event.widget.config(fg='grey')


class Base:
    def __init__(self):
        self.all = {}

    def add(self, account, key):
        account = encryption(account)
        key = encryption(key)
        self.all[account] = key
        with open('account.json', 'wb') as f:
            input_ = json.dumps(self.all, ensure_ascii=False).encode('utf-8')
            f.write(input_)
            print('message saved successfully!')
            # return f.write(input_)

    def del__(self, account):
        account = encryption(account)
        with open('account.json', 'r+') as f:
            input_ = json.load(f)
            if account in input_:
                del input_[account]


data = Base()
data.add('user', 'code')
print(data.all)


def log_in___():
    def __init__():
        if messagebox.askyesno('提示', '欢迎使用该程序!\n点击确定以进行'):
            # print('ok')
            input_account = str(input_account_1.get().strip())
            input_code = str(input_code_1.get().strip())
            input_account_2 = encryption(input_account)
            input_code_2 = encryption(input_code)
            # print(input_account_2);print(input_code_2)
            try:
                # print()
                with open('account.json', 'rb') as f:
                    check_file = json.load(f)
                    # print(check_file)
                    if check_file[input_account_2] == input_code_2:
                        root.destroy()
                        messagebox.showinfo('提示', '登陆成功,欢迎使用!')
                        #########主功能框架#########
                        progress_to_search()
                        #########主功能框架#########
                    else:
                        messagebox.showinfo('提示', '账号或密码错误!')
            except KeyError or TypeError:
                if messagebox.askyesno('提示', '系统出现错误,是否联系后台人员\n或退出?,'):
                    messagebox.showinfo('联系方式', '1111')
                else:
                    root.quit()

        else:
            messagebox.showinfo('正在退出该程序....\n感谢本次使用!!')
            root.quit()

    root = tk.Tk()
    root.title('进入程序')
    root.geometry('400x300')

    tk.Label(root, text='账号:').grid(row=1, column=0)

    input_account_1 = tk.Entry(root)
    input_account_1.default_text = '在此输入你的账号......'
    input_account_1.insert(0, input_account_1.default_text)
    input_account_1.bind('<FocusIn>', click_to_clean_column)
    input_account_1.grid(row=1, column=1, columnspan=2)

    tk.Label(root, text='密码:').grid(row=2, column=0)

    input_code_1 = tk.Entry(root, show='*')
    input_code_1.grid(row=2, column=1, columnspan=2)

    root.button = tk.Button(root, text='登录', command=__init__)
    root.button.grid(row=3, column=2)

    root.mainloop()

log_in___()
