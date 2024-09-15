from tempfile import template

from celery.bin.control import status
from django.contrib.messages import success
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django import forms

from django.shortcuts import render, redirect
from kombu.asynchronous.http import Response

from .forms import VideoUploadForm
from .models import Video, Subtitle
from .tasks import process_video

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_video.delay(video.id)  # Asynchronous task
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = VideoUploadForm()
        return JsonResponse({'success': False, 'errors': 'Invalid request method'})
from django.shortcuts import render
from .models import Video

@csrf_exempt
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        video_list = list(videos.values('id', 'file', 'uploaded_at'))  # Convert QuerySet to list of dicts
        return JsonResponse({'videos': video_list})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.db.models import Q

@csrf_exempt
def search(request):
    phrase = request.GET.get('phrase', '')
    results = []

    if phrase:
        results = Subtitle.objects.filter(content__icontains=phrase).values('id', 'video', 'language', 'content', 'created_at')
    return JsonResponse({'results': list(results)})
    # return render(request, 'video_app/video_processing/templates/videos/search.html', context)




