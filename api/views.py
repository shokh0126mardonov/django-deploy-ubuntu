from django.http import HttpRequest,HttpResponse


def TestApi(r:HttpRequest)->HttpResponse:
    return HttpResponse(content='test api')