from django.apps import AppConfig


class VideoProcessingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video_processing'

from django.apps import AppConfig

class VideosConfig(AppConfig):
    name = 'videos'

    def ready(self):
        import videos.signals
