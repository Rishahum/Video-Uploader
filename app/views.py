from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .forms import Video_form, TimestampForm
from .models import Video, Timestamp

def homePage(request):
    return render(request,"index.html")

def certificateUs(request):
    return render(request, "certificate.html")

def index(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=Video_form()
        return render(request,'certificate.html',{"form":form,"all":all_video})

def add_timestamp(request, video_id):
    video = Video.objects.get(pk=video_id)
    if request.method == 'POST':
        form = TimestampForm(request.POST)
        if form.is_valid():
            timestamp = form.save(commit=False)
            timestamp.video = video
            timestamp.save()
            return redirect('add_timestamp', video_id=video_id)
    else:
        form = TimestampForm()
    return render(request, 'certificate.html', {'form': form, 'video': video})