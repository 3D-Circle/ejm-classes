from django.shortcuts import render
import os
import markdown


def homepage(request):
    subjects_available = [x[0].split(
        "/"
    )[-1] for x in os.walk("classnotes_browser/static/classnotes_browser/md_src/")][1:]
    print(subjects_available)
    subjects_available = [["SES", "History", "French"], ["Pomme cuite"]]
    return render(request, "classnotes_browser/homepage.html", {"subj_list": subjects_available})


def render_md(request, cours, name):
    with open("/app/classnotes_browser/static/classnotes_browser/md_src/{}/{}.md".format(cours, name)) as f:
        content = markdown.markdown(f.read())
        print(content)
    return render(request, "classnotes_browser/md_display.html", {"title": name, "md_in": content})
