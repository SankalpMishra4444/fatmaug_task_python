# import subprocess
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Video
#
# @receiver(post_save, sender=Video)
# def process_video(sender, instance, **kwargs):
#     if not instance.processed:
#         # Run ccextractor here
#         subprocess.run(['ccextractor', instance.video_file.path, '-o', instance.subtitle_file.path])
#         instance.processed = True
#         instance.save()
