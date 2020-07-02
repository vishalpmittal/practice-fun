from django.shortcuts import render
from django.http import HttpResponse
from .models import RaffleGame

rg = RaffleGame()


def get_players(request):
    return HttpResponse(str(rg.list_participants()))


def issue_tickets(request):
    try:
        user = request.GET['user']
        num_of_tix = int(request.GET['tickets'])
    except:
        return HttpResponse(str({'Error': 'Invalid Parameters'}))

    return HttpResponse(str(rg.issue_tickets(user, num_of_tix)))


def transfer_tickets(request):
    try:
        donor = request.GET['donor']
        recipient = request.GET['recipient']
        num_of_tix = int(request.GET['tickets'])
    except:
        return HttpResponse(str({'Error': 'Invalid Parameters'}))

    return HttpResponse(str(rg.transfer_ticket(num_of_tix, donor, recipient)))


def draw_winner(request):
    return HttpResponse(str(rg.draw_winner()))


def new_game(request):
    return HttpResponse(str(rg.new_game()))
