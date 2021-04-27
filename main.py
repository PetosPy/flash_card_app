from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

#-------Random french words -----------------#

my_file = pd.read_csv("./data/french_words.csv")
pd_dictionary = my_file.to_dict(orient="records")
current_card = {}

def next_card():
	global current_card
	current_card = random.choice(pd_dictionary)
	canvas.itemconfigure(card_title, text="French", fill="black")
	canvas.itemconfigure(card_word, text=current_card["French"], fill="black")
	canvas.itemconfig(back_image, image=front_img )
	


def flip_card():
	canvas.itemconfigure(card_title, text="English", fill="white")
	canvas.itemconfigure(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(front_img, image=back_image )
	

#--------------- UI setup ------------#
window =  Tk()
window.title("Flash")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card )

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

flash_img = PhotoImage(file="./images/card_front.png")
front_img = canvas.create_image(400, 263,image=flash_img)
canvas.grid(row=0, column=0, columnspan=2)

back_image = PhotoImage(file="./images/card_back.png")

#-------- text on canvas ------
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))

#-------- x button -----
cross_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=cross_image, bd=0, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

#-------- y button -----
check_image = PhotoImage(file="./images/right.png")
y_button = Button(image=check_image,bd=0, highlightthickness=0, command=next_card)
y_button.grid(row=1, column=1)

next_card()








window.mainloop()


