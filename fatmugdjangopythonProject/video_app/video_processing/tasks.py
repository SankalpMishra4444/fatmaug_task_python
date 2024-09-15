from celery import shared_task
from .models import Video
import subprocess

@shared_task
def process_video(video_id):
    try:
        video = Video.objects.get(id=video_id)
        # Example command for ccextractor
        command = f"ccextractor {video.file.path} -o {video.file.path}.srt"
        subprocess.run(command, shell=True, check=True)
        # Here you should also add code to parse and save subtitles
    except Video.DoesNotExist:
        print(f"Video with id {video_id} does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
