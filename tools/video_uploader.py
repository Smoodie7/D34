import os
import threading
import random
import string
from datetime import datetime
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path

    def process_video(self):
        if os.path.isfile(self.video_path) and self.video_path.lower().endswith('.mp4'):
            folder_name = f"_{create_video_id()}"
            os.makedirs(folder_name)

            resolutions = [480, 720, 1080]

            for resolution in resolutions:
                if resolution <= self.get_video_resolution(self.video_path):
                    output_name = f"{folder_name}/videoplayback_{resolution}.mp4"
                    self.convert_video(self.video_path, output_name, resolution)

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
    video_path = input("An MP4 file (min. 480p): ").strip()
    video_processor = VideoProcessor(video_path)
    video_processor.process_video()
