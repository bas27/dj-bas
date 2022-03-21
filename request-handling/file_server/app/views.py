from datetime import datetime
import pathlib

from django.shortcuts import render
from app import settings
from os import listdir, stat


def file_list(request, dt: datetime = None):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # context = {
    #     'files': [
    #         {'name': 'file_name_1.txt',
    #          'ctime': datetime.datetime(2018, 1, 1),
    #          'mtime': datetime.datetime(2018, 1, 2)}
    #     ],
    #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    # }
    
    # dt = datetime.date(2018, 1, 1)
    context = {
        'files': get_context_list(),
        'date': dt  # Этот параметр необязательный
    }
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = f'{settings.FILES_PATH}/{name}'
    with open(file_path, 'r') as  file:
        file_read = file.read()

    return render(
        request,
        'file_content.html',
        # context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
        context={'file_name': name, 'file_content': file_read}
    )


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d %H:%M:%S')
    return formated_date

# def get_context_list():

#     context_list = []
#     for i in listdir(path=settings.FILES_PATH):
#         tmp_dict = {}
#         files_stat = stat(path=f'{settings.FILES_PATH}/{i}')
#         tmp_dict = {
#             'name': i,
#             'ctime': convert_date(files_stat.st_ctime),
#             'mtime': convert_date(files_stat.st_mtime)}
#         context_list.append(tmp_dict)
    
#     return context_list


def get_context_list():

    context_list = []
    for i in listdir(path=settings.FILES_PATH):
        tmp_dict = {}
        fname = pathlib.Path(f'{settings.FILES_PATH}/{i}')
        # files_stat = stat(path=f'{settings.FILES_PATH}/{i}')
        tmp_dict = {
            'name': i,
            'ctime': datetime.fromtimestamp(fname.stat().st_ctime),
            'mtime': datetime.fromtimestamp(fname.stat().st_mtime)}
        context_list.append(tmp_dict)
    
    return context_list