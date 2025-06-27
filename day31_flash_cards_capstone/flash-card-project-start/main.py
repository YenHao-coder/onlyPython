from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

""" VARIABLE """

to_learn = {}
current_card = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError: 
    df_original = pd.read_csv("data/french_words.csv")
    to_learn = df_original.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

"""FUNCTION"""
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(word_label, text =current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card['English'], fill="white")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=FALSE)
    next_card()
 
"""UI DESIGN"""

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background="#B1DDC6")
flip_timer = window.after(3000, func=flip_card)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg="#B1DDC6",highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)

title_label = canvas.create_text(400, 150, text="", font=(FONT_NAME, 35, "italic"))
word_label = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


known_button = Button(image=right_image,highlightthickness=0, command= is_known)
known_button.grid(row=1, column=0)
unknown_button = Button(image=wrong_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()

window.mainloop()