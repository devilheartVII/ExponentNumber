import tkinter as tk


def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='\n' + 'ได้ 0 หมดไงไอโง่')
        return

    output = ''
    for i in range(1, 21):
        output += str(number) + ' กำลัง ' + str(i)
        output += ' = ' + str(number ** i) + '\n'

    output_label.configure(text=output)


window = tk.Tk()
window.title('ExponentNumber')
window.minsize(width=400, height=500)

title_label = tk.Label(master=window, text='เลขยกกำลัง')
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=20)
number_input.pack(pady=5)

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=show_output, width=5, height=1
)
go_button.pack(pady=8)

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
