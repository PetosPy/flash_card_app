from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

#-------Random french words -----------------#

my_file = pd.read_csv("./data/french_words.csv")
pd_dictionary = my_file.to_dict(orient="records")


def next_card():
	card = random.choice(pd_dictionary)
	canvas.itemconfigure(card_title, text="French")
	canvas.itemconfigure(card_word, text=card["French"])


	# canvas.itemconfig(front_img, image=back_image )
	# canvas.itemconfigure(card_title, text="English")
	# canvas.itemconfigure(card_word, text=card["English"])




#--------------- UI setup ------------#
window =  Tk()
window.title("Flash")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

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


