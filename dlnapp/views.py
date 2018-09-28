from django.shortcuts import render

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
