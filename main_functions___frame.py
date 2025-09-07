import tkinter as tk
from tkinter import ttk,messagebox

from 已完成.接单平台汇集.main_functions____paltforms_content import collage_student_help, cheng_xv_yuan_net, hai_gui
from 已完成.接单平台汇集.main_functions___platforms_frame import search_something


def progress_to_search():
    def ensure_whether_student():
        if messagebox.askyesno('提示','是否进入大学生指导页面？'):
            print('aaa')
            messagebox.showinfo('请搜索',f'{collage_student_help()}')
        else:
            return

    def ensure_whether_it():
        if messagebox.askyesno('提示','是否有进入程序员专页？'):
            messagebox.showinfo('请搜索',f'{cheng_xv_yuan_net()}')
        else:
            return

    def ensure_whether_hai_gui():
        if messagebox.askyesno('提示','是否进入海归人员专页？'):
            messagebox.showinfo('请搜索',f'{hai_gui()}')
        else:
            return

    def ensure_search_normally():

        if messagebox.askyesno('提示','是否进入常规搜索？'):
            progress_root.destroy()
            progress_root.quit()
            #######常规搜索########
            search_something()
            #######常规搜索########

        else:
            return

    def quit_progress():
        if messagebox.askyesno('提示','确认退出?'):
            messagebox.showinfo('退出成功','感谢使用??')
            progress_root.quit()

    progress_root = tk.Tk()
    progress_root.title('准备搜索界面')
    progress_root.geometry('400x600')

    progress_button = tk.Button(progress_root,text='我是大学生',command=ensure_whether_student)
    progress_button.pack()

    progress_button_1 = tk.Button(progress_root,text='我是程序员',command=ensure_whether_it)
    progress_button_1.pack()

    progress_button_2 = tk.Button(progress_root,text='我是海归人员',command=ensure_whether_hai_gui)
    progress_button_2.pack()

    progress_button_3 = tk.Button(progress_root,text='进入常规搜索',command =ensure_search_normally)
    progress_button_3.pack()

    tk.Label(progress_root, text='请根据以上选项进行慎重选择\n以便尽可能对您有用！！').pack()

    progress_button_4 = tk.Button(progress_root,text='退出',command=quit_progress)
    progress_button_4.pack()

    progress_root.mainloop()

# progress_to_search()
