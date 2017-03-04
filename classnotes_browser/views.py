from django.shortcuts import render
from django.http import HttpResponse
import os


# def index(request):
#     return render(request, "classnotes_browser/homepage.html")

def homepage(request):
    subjects_available = [x[0].split(
        "/"
    )[-1] for x in os.walk("classnotes_browser/static/classnotes_browser/md_src/")][1:]
    print(subjects_available)
    return render(request, "classnotes_browser/homepage.html")