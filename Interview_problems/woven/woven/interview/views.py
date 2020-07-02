from django.http import HttpResponse
from interview.rest_worker import RESTWorker
from interview.models import Inbox

inbox = Inbox()
inbox.load_emails_from_file()


def index(request):
    # rw = RESTWorker()
    # suits = '<br/>'
    # for f_name in sorted(rw.get_all_users()):
    #     suits += rw.get_full_name(f_name) + '<br/>'
    #
    # return HttpResponse(suits)

    fp = open('/Users/vishalm/Downloads/winequality-white.csv', 'r')
    first_line = fp.readline()
    resp = ''
    for _ in range(3):
        resp += fp.readline()

    print(resp)
    return HttpResponse("<br/>Here's the wine testing 3 lines:<br/>" + resp)

    # return HttpResponse("i am in the interview app")


def flat_inbox(request):
    return HttpResponse(inbox.get_all_emails())


def threaded_inbox(request):
    return HttpResponse(inbox.get_all_emails_threaded())
