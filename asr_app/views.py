from django.shortcuts import render


def index(request):
    return render(request, "asr_app/index.html")
