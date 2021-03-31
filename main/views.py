from django.http import HttpResponse
from django.shortcuts import render

from . import conimg, eval

global img1, img2


def home(req):
    return render(req, '../templates/home/index.html')


def omrs(req):
    if req.method == 'POST' and req.FILES['upload_img']:
        global img1
        img1 = conimg.resize_img(req.FILES['upload_img'])

    return render(req, 'omrs/index.html')


def show(req):
    if req.method == 'POST' and req.FILES['upload_img']:
        global img1, img2
        img2 = conimg.resize_img(req.FILES['upload_img'])
        img = eval.eval(img1, img2)

        return render(req, 'show/index.html', {'img': "data:image/jpg;base64," + img})
    else:
        return HttpResponse('<center><h1>not found !</h1></center>')


def about(req):
    return render(req, 'about/index.html')
