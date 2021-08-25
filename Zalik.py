from tkinter import *
from math import pow, atan

window = Tk()
window.title("Залік")
window.geometry('400x400')
lbl_z = Label(window, text="z = ")
lbl_z.grid(column=0, row=0)

input_z = Entry(window, width=7, textvariable="0")
input_z.grid(column=1, row=0)

input_e = Entry(window, width=7)
input_e.grid(column=1, row=1)

lbl_e = Label(window, text="ε = ")
lbl_e.grid(column=0, row=1)

lbl_file = Label(window, text="Введіть назву файлу для збереження: ")
lbl_file.grid(column=0, row=2)

input_file_name = Entry(window, width=20)
input_file_name.grid(column=1, row=2)

def clicked() :
    try:
        print(not (abs(float(input_z.get())) < 1) and not ((float(input_e.get()) > 0) and (float(input_e.get()) < 1)))
        if not (abs(float(input_z.get())) < 1) or not ((float(input_e.get()) > 0) and (float(input_e.get()) < 1)):
            lbl_error = Label(window, text="Введено недопустимі дані")
            lbl_error.grid(column=0, row=4)

            file_name = f"{input_file_name.get()}.txt"
            with open(file_name, 'w') as file_object:
                file_object.write("Wrong data")

            raise IllegalArgumentException("Введено недопустимі дані")
        else:
            lbl_result_python = Label(window, text=f"Очікуваний результат: {atan(float(input_z.get()))}")
            lbl_result_python.grid(row=6)
            result = count(0,0)
            lbl_result = Label(window, text=f"Результат розрахунку: {result[0]}")
            lbl_result.grid(row=4)
            lbl_result2 = Label(window, text=f"Кількість використаних доданків: {result[1]}")
            lbl_result2.grid(row=5)

            file_name = f"{input_file_name.get()}.txt"
            with open(file_name, 'w') as file_object:
                file_object.write(f"z = {input_z.get()} "
                                  f"\ne = {str(input_e.get())}"
                                  f"\nОчікуваний результат: {atan(float(input_z.get()))}"
                                  f"\nРезультат розрахунку: {result[0]}"
                                  f"\nКількість використаних доданків: {result[1]}")

    except ValueError:
        error_lbl = Label(window, text="Невірно введені дані")
        error_lbl.grid(column=0, row=4)

def count(n=0, counting=0): # проверим
    e = pow(-1, n) * ((pow(float(input_z.get()), (2 * n + 1)))/(2 * n + 1))
    if (abs(e) > float(input_e.get())):
        counting = counting + e
        return count(n + 1, counting)
    result = [counting, (n + 1)]
    return result

class IllegalArgumentException(Exception) :
    def __init__(self, text):
        self.text = text

btn = Button(window, text="Розрахувати", command=clicked)
btn.grid(row=3)

window.mainloop()