from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def dln(request):
    data = {"description": "Регистрация, сертификация и декларирование медицинских изделий и БАДов", "title": "Регистрация медицинских изделий", "formtext": "Возник вопрос и хотите получить консультацию?"}
    return render(request, 'html/index.html', context=data)


def declarate(request):
    data = {"description": "Декларирование", "title": "Декларирование", "formtext": "Хотите получить услугу по декларированию?"}
    return render(request, 'html/declarate.html', context=data)


def lp(request):
    data = {"description": "Лекарственные препараты", "title": "Лекарственные препараты", "formtext": "Хотите получить услугу по регистрации лп?"}
    return render(request, 'html/lp.html', context=data)


def mi(request):
    data = {"description": "Медицинские изделия", "title": "Медицинские изделия", "formtext": "Хотите зарегистрировать медицинское изделие?"}
    return render(request, 'html/mi.html', context=data)


def bad(request):
    data = {"description": "Биологически активные добавки", "title": "Биологически активные добавки", "formtext": "Хотите зарегистрировать БАД?"}
    return render(request, 'html/bad.html', context=data)


def registration(request):
    data = {"description": "Регистрация медицинских изделий и БАДов", "title": "Регистрация", "formtext": "Хотите зарегистрировать мед. изделие или БАД?"}
    return render(request, 'html/registration.html', context=data)


def sertification(request):
    data = {"description": "Сертификация", "title": "Сертификация", "formtext": "Хотите произвести сертификацию?"}
    return render(request, 'html/sertification.html', context=data)

def ls(request):
    data = {"description": "Сертификация", "title": "Сертификация"}
    return render(request, 'html/ls.html', context=data)

def medprod(request):
    data = {}
    return render(request, 'html/medical-products.html')

def disprod(request):
    data = {}
    return render(request, 'html/disinfecting-products.html')

def sportpit(request):
    data = {}
    return render(request, 'html/sport-nutrition.html')

def cosprod(request):
    data = {}
    return render(request, 'html/cosmetic-products.html')

def rawforbad(request):
    data = {}
    return render(request, 'html/raw-for-bad.html')

def otherbad(request):
    data = {}
    return render(request, 'html/other-bad.html')

def foodstuffs(request):
    data = {}
    return render(request, 'html/foodstuffs.html')

def regmedecine(request):
    data = {}
    return render(request, 'html/register-medecine.html')

def regmedecinerf(request):
    data = {}
    return render(request, 'html/register-medecine-RF.html')

def makechanges(request):
    data = {}
    return render(request, 'html/make-changes.html')

def regmedecineeeu(request):
    data = {}
    return render(request, 'html/register-medicine-eeu.html')

def regbad(request):
    data = {}
    return render(request, 'html/register-bad.html')

def regcosmeticproducts(request):
    data = {}
    return render(request, 'html/register-cosmetic-products.html')

def licenseformedicine(request):
    data = {}
    return render(request, 'html/license-for-medicine.html')

def licensemedicaltechnique(request):
    data = {}
    return render(request, 'html/license-medical-technique.html')

def certificationiso(request):
    data = {}
    return render(request, 'html/certification-iso.html')

def certificationeeu(request):
    data = {}
    return render(request, 'html/certification-eeu.html')

def declarateandcertificate(request):
    data = {}
    return render(request, 'html/declarate-and-certificate.html')

def documents(request):
    data = {}
    return render(request, 'html/documents.html')

def contact(request):
    data = {}
    return render(request, 'html/contact.html')

def reviews(request):
    data = {
        "reviewsList": [
            'img/reviews/1.png',
            'img/reviews/2.png',
            'img/reviews/3.png',
            'img/reviews/4.jpg',
            'img/reviews/5.jpg',
            'img/reviews/6.jpg',
            'img/reviews/7.jpg',
            'img/reviews/8.png',
            'img/reviews/9.png',
            'img/reviews/10.png',
            'img/reviews/11.png',
            'img/reviews/12.png',
            'img/reviews/13.png',
            'img/reviews/14.png',
            'img/reviews/15.png',
            'img/reviews/16.png'
        ],
        "logos": [
            'img/logo/1.jpg',
            'img/logo/2.png',
            'img/logo/3.jpg',
            'img/logo/4.jpg',
            'img/logo/5.png',
            'img/logo/6.png',
            'img/logo/7.jpg',
            'img/logo/8.jpg',
            'img/logo/9.jpg',
            'img/logo/10.jpg',
            'img/logo/11.jpg',
            'img/logo/12.jpg',
            'img/logo/13.jpg',
            'img/logo/14.jpg',
            'img/logo/15.png',
            'img/logo/16.jpg',
            'img/logo/17.jpg',
            'img/logo/18.jpg',
            'img/logo/19.jpg',
            'img/logo/20.png',
            'img/logo/21.png',
            'img/logo/22.png',
            'img/logo/23.png',
            'img/logo/24.png',
            'img/logo/25.png',
            'img/logo/26.png',
            'img/logo/27.png',
            'img/logo/28.jpg',
            'img/logo/29.jpg',
            'img/logo/30.jpg',
            'img/logo/31.jpg',
            'img/logo/32.jpg',
            'img/logo/33.png',
            'img/logo/34.jpg',
            'img/logo/35.jpg',
            'img/logo/36.jpg',
            'img/logo/37.jpg',
            'img/logo/38.png',
            'img/logo/39.jpg',
        ]
    }
    return render(request, 'html/reviews.html', context=data)

def message(request):
    answer = dict()
    # session_key = request.session.session_key
    print(request.POST.get('phone'))
    subject = 'Заказ с сайта DLN'
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mess = "\r\n".join((
        "Имя клиента: %s" % name,
        "Телефон или почта: %s" % phone
    ))
    if name and phone:
        try:
            send_mail(subject, mess, 'centr-dln@yandex.ru', ['centr-dln@yandex.ru'])
            print('message successfuly sent')
        except BadHeaderError:
            return HttpResponse('Error send mail')
    else:
        return HttpResponse('All fields valid?')
    return JsonResponse(answer)
