from datetime import datetime
import pathlib

from django.shortcuts import render
from app import settings
from os import listdir

def file_list(request, date: datetime = None):
    template_name = 'index.html'

    context = {
        'files': get_context_list(),
        'date': date
    }
    return render(request, template_name, context)


def file_content(request, name):

    file_path = f'{settings.FILES_PATH}/{name}'
    with open(file_path, 'r') as file:
        file_read = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_read}
    )


def get_context_list():

    context_list = []
    for i in listdir(path=settings.FILES_PATH):
        tmp_dict = {}
        fname = pathlib.Path(f'{settings.FILES_PATH}/{i}')

        tmp_dict = {
            'name': i,
            'ctime': datetime.fromtimestamp(fname.stat().st_ctime),
            'mtime': datetime.fromtimestamp(fname.stat().st_mtime)}
        context_list.append(tmp_dict)

    return context_list