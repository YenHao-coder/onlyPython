from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
test = ['a ', ' kd', 'de', 
        'c ', 'b ', 'd ',
        'r']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', "&", '(', ')', '*', '+']
# ---------------------------- LOOK UP PASSWORD ------------------------------- #
def find_password():
    wesite = web_entry.get()
    email = mail_entry.get()
    pswrd = password_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    
    except FileNotFoundError:
        messagebox.showinfoprint(title="Error", message="No Data File Found.")
    
    else:
        if(wesite in data):
            website = web_entry.get()
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Mail: {email},\n Password: {password}" )
        else:
            print(f"No Details for the {website} exists.")
    finally:
        file.close()
    
# ---------------------------- GENERRATE PASSWORD ------------------------------- #
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
    data_json = {website:{"email":email,"password":pswrd}}
    
    if len(website) == 0 or len(email) ==0 or len(pswrd) == 0:
        empty_web = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entried: Website:\nEmail: {email}\nPassword:{pswrd}\nIs it ok to save? ")
        
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data=json.load(data_file) #reading old data
                
            except FileNotFoundError:                   
                with open("data.json", "w") as data_file:
                    json.dump(data_json, data_file, indent=4)

            else:
                data.update(data_json) #updating old data with new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                web_entry.delete(0,END)
                password_entry.delete(0,END)
                data_file.close() 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("passwaordManager")
window.config(padx=50, pady=50)

canvas = Canvas(width=153, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(80, 100, image=lock_img)

web_label = Label(text="Website:")
mail_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
web_entry = Entry(width=20)
mail_entry = Entry(width=39)
password_entry = Entry(width=20)
password_button = Button(text="Generate Password", command=pswrd_gen)
search_button = Button(text="Search", width=15, command=find_password)
add_button = Button(text="Add", width=38, command=save)

web_entry.focus()
mail_entry.insert(0,"andy@email.com")

canvas.grid(row=0, column=1)
web_label.grid(row=1, column=0)
mail_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
web_entry.grid(row=1, column=1, sticky="w")
mail_entry.grid(row=2, column=1, columnspan=2, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
search_button.grid(row=1, column=2)
password_button.grid(row=3, column=2, sticky="e")

window.mainloop()