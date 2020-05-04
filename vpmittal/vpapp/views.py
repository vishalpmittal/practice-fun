from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest, HttpResponse, Http404
from django.conf import settings
import os
from .utils import file_utils


class VPView(View):
    http_method_name = ['get', 'post', 'put', 'delete']

    def get(self, *args, **kwargs):
        request = args[0]
        return HttpResponse(str(
            {"Sucess": "You called the get api with param: {}".format(
                request.GET.get('param')
            )})
        )

    def post(self, *args, **kwargs):
        request = args[0]
        return HttpResponse(str(
            {"Sucess": "You called the post with param: {}, {}".format(
                request.GET.get('paramg'),
                request.POST.get('paramp'),    # to read form data
                # request.body             # to read request body
            )})
        )

    def put(self, *args, **kwargs):
        request = args[0]
        return HttpResponse(str(
            {"Sucess": "You called the put with param: {}, {}".format(
                request.GET.get('param'),
                request.body
            )})
        )

    def delete(self, *args, **kwargs):
        request = args[0]
        return HttpResponse(str(
            {"Sucess": "You called the delete with param: {}".format(
                request.GET.get('param')
            )})
        )


def read_file(request):
    file_path = os.path.join(settings.TEST_DATA_PATH, 'most_common_words.txt')
    return HttpResponse(str(file_utils.read_data(file_path)))


def download_file(request):
    file_path = os.path.join(settings.TEST_DATA_PATH, 'most_common_words.txt')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
