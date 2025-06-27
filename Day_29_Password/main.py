from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', "&", '(', ')', '*', '+']

def pswrd_gen():

    letter_list = [choice(letters) for _ in range(randint(8,10))]
    symbols_list = [choice(letters) for _ in range(randint(2,4))]
    numbers_list = [choice(letters) for _ in range(randint(2,4))] 

    # 打亂列表內排序
    password_list = letter_list+symbols_list+numbers_list
    shuffle(password_list) 

    # 產生密碼
    password = "".join(password_list) 

    print(f"Your password is : {password}")
    # 密碼插入輸入欄位
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # 保存密碼並生成txt檔
    website = web_entry.get()
    email = mail_entry.get()
    pswrd = password_entry.get()
    
    if len(website) == 0 or len(email) ==0 or len(pswrd) == 0:
        empty_web = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entried: Website:\nEmail: {email}\nPassword:{pswrd}\nIs it ok to save? ")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website} | {email} | {pswrd} \n")
            web_entry.delete(0,END)
            password_entry.delete(0,END)
            file.close()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("passwaordManager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

web_label = Label(text="Website:")
mail_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
web_entry = Entry(width=35)
mail_entry = Entry(width=35)
password_entry = Entry(width=18)
password_button = Button(text="Generate Password", command=pswrd_gen)
add_button = Button(text="Add", width=35, command=save)

web_entry.focus()
mail_entry.insert(0,"andy@email.com")

canvas.grid(row=0, column=1)
web_label.grid(row=1, column=0)
mail_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
web_entry.grid(row=1, column=1, columnspan=2)
mail_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
add_button.grid(row=4, column=1, columnspan=2)
password_button.grid(row=3, column=2)


window.mainloop()