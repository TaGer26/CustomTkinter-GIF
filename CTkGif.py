from customtkinter import *
from PIL import Image

class CTkGif():
    def __init__(self, window: any, file_path: str, update_speed: int=15, debug=False):
        self.window, self.playing, self.frame, self.update_speed, self.debug = window, False, 0, update_speed, debug

        self.gif_file = Image.open(file_path)
        self.frames, self.size = self.gif_file.n_frames, self.gif_file.size
        self.widget = CTkLabel(self.window, text='', image=CTkImage(dark_image=self.gif_file, size=(self.size)))
    def configure(self, file_path: str=None):
        if file_path:
            self.gif_file = Image.open(file_path)
            self.frames, self.size = self.gif_file.n_frames, self.gif_file.size
    def toggle(self, type: bool=None):
        if type:
            self.playing = type
            self.update()
        else:
            if self.playing: self.playing = False
            elif not self.playing:
                self.playing = True
                self.update()
        return self.playing
    def update(self):
        if self.playing:
            if self.frame < self.frames:
                self.gif_file.seek(self.frame)
                self.widget.configure(image=CTkImage(dark_image=self.gif_file, size=self.size))
                self.frame += 1
            else: self.frame = 0
            self.window.after(self.update_speed, self.update)
