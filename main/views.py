from django.shortcuts import render

from . import conimg, eval, models

global img1, img2


def home(req):
    if req.method == 'POST' and req.FILES['upload_img']:
        global img1
        img1 = conimg.resize_img(req.FILES['upload_img'])

    return render(req, '../templates/home/index.html')


def omrs(req):
    if req.method == 'POST' and req.FILES['upload_img']:
        global img1, img2
        img2 = conimg.resize_img(req.FILES['upload_img'])
        img2 = eval.eval(img1, img2)

    return render(req, 'omrs/index.html')


def show(req):
    return render(req, 'show/index.html', {'img': "data:image/jpg;base64," + img2})


def about(req):
    return render(req, 'about/index.html')


def support(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        amount = req.POST.get('amount')
        entry = models.Donor(name=name, email=email, amount=amount)
        entry.save()

    return render(req, 'make-me-happy/index.html')
