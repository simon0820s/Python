from django.http import HttpResponse
import datetime

def age(request,age):
    if age>=18:
        if age>=60:
            category="tercera edad"
        else:
            category="mayor de edad"
    else:
        category="menor de edad"

    result="<h1>Categoria de edad: %s</h1>"%category

    return HttpResponse(result)

def now(request):
    response="<h1> momento actual es: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))    
    return HttpResponse(response)