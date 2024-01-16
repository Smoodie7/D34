import random
import string

video_release_date = 100223231032

def create_video_id(video_release_date):
    letters = string.ascii_letters
    random_str = ''.join(random.choice(letters) for i in range(6))
    video_id = f'{random_str}x{video_release_date}'

    return video_id
 