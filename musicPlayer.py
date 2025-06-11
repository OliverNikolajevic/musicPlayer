
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

pygame.mixer.init()

current_volume = 50

def load_song():
    global current_song
    path = filedialog.askopenfilename(filetypes=[("Аудио Фајлови", "*.mp3;*.wav")])
    if path:
        try:
            pygame.mixer.music.load(path)
            current_song = path.split("/")[-1]
            lbl_song.config(text=f"🎵 {current_song}")
            lbl_status.config(text="Фајлот е вчитан")
        except Exception as e:
            messagebox.showerror("Грешка", f"Не може да се вчита фајлот: {e}")

def play_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    try:
        pygame.mixer.music.play()
        lbl_status.config(text="▶️ Се репродуцира")
    except:
        messagebox.showwarning("Внимание", "Прво треба да вчиташ песна!")

def pause_song():
    pygame.mixer.music.pause()
    lbl_status.config(text="⏸️ Паузирано")

def unpause_song():
    pygame.mixer.music.unpause()
    lbl_status.config(text="▶ Продолжено")

def stop_song():
    pygame.mixer.music.stop()
    lbl_status.config(text="⏹ Сопрено")

def set_volume(val):
    volume=float(val)/100
    pygame.mixer.music.set_volume(volume)

# Tkinter window
window = tk.Tk()
window.title("Audio player")
window.geometry("320x320")
window.configure(bg="black")

lbl_song = tk.Label(window, text="Нема вчитана песна", font=("Arial", 12, "bold"), fg="white", bg="black")
lbl_song.pack(pady=12)

btn_bg = "gray"
btn_fg = "white"

tk.Button(window, text="🎵 Вчитај песна", command=load_song, bg=btn_bg, fg=btn_fg, width=15).pack(pady=3)
tk.Button(window, text="▶️ Пушти", command=play_song, bg=btn_bg, fg=btn_fg, width=15).pack(pady=3)
tk.Button(window, text="⏸️ Паузирај", command=pause_song, bg=btn_bg, fg=btn_fg, width=15).pack(pady=3)
tk.Button(window, text="▶ Продолжи", command=unpause_song, bg=btn_bg, fg=btn_fg, width=15).pack(pady=3)

lbl_status = tk.Label(window, text="Статус: ---", fg="lightgray", bg="black")
lbl_status.pack(pady=10)

tk.Label(window, text="🔊 Јачина", fg="white", bg="black").pack()
volume_slider = tk.Scale(window, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL, length=200,
                         command=set_volume, bg="black", fg="white")
volume_slider.set(current_volume)
volume_slider.pack(pady=5)

window.mainloop()