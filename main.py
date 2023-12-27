import tkinter as tk
from tkinter import messagebox
import random
import time
import pygame


def close():
    pygame.mixer.music.stop()
    window.destroy()


def generate_key_variant1():
    key = ''
    for _ in range(3):
        key += ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3))
        key += ''.join(random.sample('0123456789', 2))
        key += '-'
    key = key[:-1]
    return key


def verify_key(input_key):
    generated_key = lbl_result.cget("text")
    if input_key == generated_key:
        messagebox.showinfo("Identity Approved", "Access Granted")
        window.destroy()
    else:
        pygame.mixer.music.load('Pubg Bomb.mp3')
        pygame.mixer.music.play(0)
        messagebox.showinfo("Bomb Exploded", "Access Denied")
        window.destroy()


def update_timer():
    remaining_time = int((time_remaining - (time.time() - start_time)))
    timer_label.configure(text=f"Time remaining: {remaining_time} seconds")
    if remaining_time > 0:
        window.after(1000, update_timer)
    else:
        pygame.mixer.music.load('Pubg Bomb.mp3')
        pygame.mixer.music.play(0)
        start_timer()


def start_timer():
    pygame.mixer.music.load('Pubg Bomb.mp3')
    pygame.mixer.music.play(0)
    messagebox.showinfo("Time's up!", "Bomb Exploded")
    window.destroy()


def calc():
    input_key = user_input.get()
    verify_key(input_key)


# pygame mixer for music
pygame.mixer.init()
pygame.mixer.music.load('pubg-theme-song.mp3')
pygame.mixer.music.play(-1)

window = tk.Tk()
window.geometry('1920x1080')

bg_img = tk.PhotoImage(file='pubggg.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_heading = tk.Label(frame, text='INPUT KEY TO DEACTIVATE THE BOMB', font=('Arial', 12))
lbl_heading.grid(column=1, row=0, columnspan=2, pady=10)

lbl_roots = tk.Label(frame, text='Generated Key:')
lbl_roots.grid(column=1, row=2)
generated_key = generate_key_variant1()
lbl_result = tk.Label(frame, text=generated_key, font=('Arial', 10))
lbl_result.grid(column=2, row=2)

user_input = tk.Entry(frame, width=30)
user_input.grid(column=1, row=3, columnspan=2, padx=10, pady=15)

btn_calc = tk.Button(frame, text='Verify Key', command=calc)
btn_calc.grid(column=1, row=4, columnspan=2, padx=10, pady=15)

btn_exit = tk.Button(frame, text='Exit', command=close)
btn_exit.grid(column=1, row=5, columnspan=2, padx=10, pady=15)

timer_label = tk.Label(frame, text="Time remaining: 60 seconds")
timer_label.grid(column=1, row=6, columnspan=2, pady=10)

start_time = time.time()
time_remaining = 60
update_timer()

window.mainloop()
