from django.shortcuts import render
from django.http import HttpResponse


def wine_quality(request):
    fp = open('winequality-white.csv', 'r')
    first_line = fp.readline()
    resp = ''
    for _ in range(3):
        resp += fp.readline()

    print(resp)
    return HttpResponse("<br/>Here's the wine testing 3 lines:<br/>" + resp)
