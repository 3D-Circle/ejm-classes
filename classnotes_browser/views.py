from django.shortcuts import render
import os


# def index(request):
#     return render(request, "classnotes_browser/homepage.html")

def homepage(request):
    subjects_available = [x[0].split(
        "/"
    )[-1] for x in os.walk("classnotes_browser/static/classnotes_browser/md_src/")][1:]
    print(subjects_available)
    subjects_available = [["SES", "History", "French"], ["Pomme cuite"]]
    return render(request, "classnotes_browser/homepage.html", {"subj_list": subjects_available})


def render_md(request, cours, name):
    with open("classnotes_browser/static/classnotes_browser/md_src/{}/{}.md".format(cours, name)) as f:
        content = f.read().replace("`", "")
    return render(request, "classnotes_browser/md_display.html", {"title": name, "md_in": content})
