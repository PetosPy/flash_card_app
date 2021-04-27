from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
	my_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFountError:
	original_data = pd.read.read_csv("./data/french_words.csv")
	to_learn = original_data.to_dict(orient=records)
else:
	to_learn = my_file.to_dict(orient="records")
	


def next_card():
	global current_card
	global flip_timer
	window.after_cancel(flip_timer)

	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=current_card["French"], fill="black")
	canvas.itemconfig(image_background, image=side_a)
	flip_timer = window.after(3000, func=flip_card )
	

def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(image_background, image=side_b)


def is_known():
	to_learn.remove(current_card)
	data = pd.DataFrame(to_learn)
	data.to_csv("./data/words_to_learn.csv", index=False)


	next_card()


#--------------- UI setup ------------#
window =  Tk()
window.title("Flash")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card )

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

side_a = PhotoImage(file="./images/card_front.png")
side_b = PhotoImage(file="./images/card_back.png")
image_background = canvas.create_image(400, 263,image=side_a)

canvas.grid(row=0, column=0, columnspan=2)

#-------- text on canvas ------
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))

#-------- x button -----
cross_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=cross_image, bd=0, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

#-------- y button -----
check_image = PhotoImage(file="./images/right.png")
y_button = Button(image=check_image,bd=0, highlightthickness=0, command=is_known)
y_button.grid(row=1, column=1)

next_card()








window.mainloop()


