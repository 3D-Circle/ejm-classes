from django.shortcuts import render
import markdown
import glob
import platform


MD_ROOT = "classnotes_browser/static/classnotes_browser/md_src/"
separator = "/" if platform.system() != "Windows" else "\\"


def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]


def homepage(request):
    """list the subjects available"""
    subjects_available = [
        i.split(separator)[-2] for i in glob.glob("{}*/".format(MD_ROOT))
    ]
    subjects_available = chunker(subjects_available, 3)
    print(subjects_available)
    return render(request, "classnotes_browser/homepage.html", {"subj_list": subjects_available})


def cours_dir(request, subject):
    """list the cours available for a given subject"""
    cours_available = chunker(
        [i.split(separator)[-1].split(".")[0] for i in glob.glob("{}/{}/*".format(MD_ROOT, subject)) if "." in i],
        3
    )
    return render(
        request,
        "classnotes_browser/cours_list.html",
        {
            "title": subject, "cours_list": [[
                {
                    "name": name.replace("_", " "), "link": name
                } for name in triplet] for triplet in cours_available
            ]
        }
    )


def render_md(request, cours, name):
    with open("{}{}/{}.md".format(MD_ROOT, cours, name)) as f:
        content = markdown.markdown(f.read())
    return render(request, "classnotes_browser/md_display.html", {"title": name, "md_in": content})
