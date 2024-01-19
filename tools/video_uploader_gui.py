import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import threading
import random
import string
from datetime import datetime
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Processor")

        self.label = tk.Label(root, text="Drag and drop an MP4 file (min. 480p):")
        self.label.pack(pady=10)

        self.video_path = tk.StringVar()
        self.video_entry = tk.Entry(root, textvariable=self.video_path, width=50, state='readonly')
        self.video_entry.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=200, bg="lightgray", bd=2, relief="solid")
        self.canvas.pack(pady=10)

        self.process_button = tk.Button(root, text="Process Video", command=self.process_video)
        self.process_button.pack(pady=10)

        # Drag and drop functionality
        self.video_entry.drop_target_register(DND_FILES)
        self.video_entry.dnd_bind('<<Drop>>', self.handle_drop)

    def handle_drop(self, event):
        self.video_path.set(event.data)
        self.display_thumbnail()

    def display_thumbnail(self):
        # Display video thumbnail (Pillow)
        pass

    def process_video(self):
        if self.video_path.get():
            threading.Thread(target=self.process_video_thread).start()

    def process_video_thread(self):
        video_path = self.video_path.get()
        if os.path.isfile(video_path) and video_path.lower().endswith('.mp4'):
            folder_name = f"_{create_video_id}"
            os.makedirs(folder_name)

            resolutions = [480, 720, 1080]

            for resolution in resolutions:
                if resolution <= self.get_video_resolution(video_path):
                    output_name = f"{folder_name}/videoplayback_{resolution}.mp4"
                    self.convert_video(video_path, output_name, resolution)

    def get_video_resolution(self, video_path):
        clip = VideoFileClip(video_path)
        return clip.size[1]  # Assuming the height represents the resolution

    def convert_video(self, input_path, output_path, resolution):
        clip = VideoFileClip(input_path)
        clip_resized = clip.resize(height=resolution)
        clip_resized.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=4)
        clip.close()

def create_video_id():
    current_datetime = datetime.now()
    # Format the datetime as a single number string
    video_release_date = current_datetime.strftime("%d%m%Y%H%M")

    letters = string.ascii_letters
    random_str = ''.join(random.choice(letters) for i in range(6))
    video_id = f'{random_str}x{video_release_date}'

    return video_id

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = VideoProcessor(root)
    root.mainloop()
