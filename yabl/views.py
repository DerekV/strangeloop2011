from django.http import HttpResponse


def author_list(request):
    return HttpResponse("hello, world!");
