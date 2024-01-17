from tkinter import *
import pygame
import random

BACK_GROUND = "#FFE3B3"
FORE_GROUND = "#53D2DC"

pygame.mixer.init()
window = Tk()
window.title("DJ Khaled Quotes")
window.config(bg=BACK_GROUND, padx=30, pady=30)


def next_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    random_quote = random.choice(quotes)

    canvas.itemconfig(quote_text, text=random_quote.strip())
    pygame.mixer.music.load("Dj-Khaled_audio.mp3")
    pygame.mixer.music.play()


canvas = Canvas(width=500, height=400, bg=FORE_GROUND, border=0, borderwidth=0, background=FORE_GROUND,
                highlightbackground=FORE_GROUND)
quote_text = canvas.create_text(250, 200, text="ANOTHER ONE", font=("Arial", 16, "bold"), fill=BACK_GROUND,
                                width=400)
quote_img = PhotoImage(file="./Quotes2.png", width=500, height=500)
canvas.create_image(250, 200, image=quote_img)
canvas.grid(row=0, column=0, pady=50)

khaled_img = PhotoImage(file="./DJ-Khaled.png", width=225, height=224)
button = Button(image=khaled_img, highlightthickness=0, borderwidth=0, border=0, bg=BACK_GROUND,
                background=BACK_GROUND, activebackground=BACK_GROUND, command=next_quote)
button.grid(row=1, column=0)

window.mainloop()
