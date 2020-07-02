from django.db import models
from threading import Lock
import random


class RaffleGame:
    def __init__(self):
        self.__tix_num_lock = Lock()
        self.__player_update_lock = Lock()
        self.__tix_update_lock = Lock()
        self.__transfer_lock = Lock()

        self.player_to_tixs = {}
        self.tix_to_player = {}

        self.__ticket_start_indx = 1001
        self.__next_ticket_num = self.__ticket_start_indx

    def new_game(self):
        self.__tix_num_lock.acquire()
        self.__player_update_lock.acquire()
        self.__tix_update_lock.acquire()
        self.__transfer_lock.acquire()

        self.player_to_tixs = {}
        self.tix_to_player = {}
        self.__next_ticket_num = self.__ticket_start_indx

        self.__tix_num_lock.release()
        self.__player_update_lock.release()
        self.__tix_update_lock.release()
        self.__transfer_lock.release()

        return {'Success': 'New Raffle Game Started!'}

    def list_participants(self):
        return self.player_to_tixs

    def __get_next_ticket_num(self):
        self.__tix_num_lock.acquire()
        curr_num = self.__next_ticket_num
        self.__next_ticket_num += 1
        self.__tix_num_lock.release()
        return curr_num

    def __add_ticket_to_player(self, player: str, tix_num: int):
        self.__player_update_lock.acquire()
        self.__tix_update_lock.acquire()

        self.player_to_tixs[player] = self.player_to_tixs.get(player, set())
        if tix_num in self.tix_to_player:
            curr_holding_player = self.tix_to_player[tix_num]
            self.player_to_tixs[curr_holding_player].remove(tix_num)
        self.tix_to_player[tix_num] = player
        self.player_to_tixs[player].add(tix_num)

        self.__player_update_lock.release()
        self.__tix_update_lock.release()

    def __check_n_remove_player(self, player: str):
        self.__player_update_lock.acquire()
        if player and len(self.player_to_tixs.get(player, set())) == 0:
            del self.player_to_tixs[player]
        self.__player_update_lock.release()

    def issue_tickets(self, player: str, num_of_tix: int):
        if not player or num_of_tix < 1:
            return {'Error': 'Invalid Parameters'}

        for _ in range(num_of_tix):
            curr_num = self.__get_next_ticket_num()
            self.__add_ticket_to_player(player, curr_num)

        return {'Sucess: Alloted {} tickets to user {}'.format(num_of_tix, player)}

    def transfer_ticket(self, num_of_tix: int, donor_player: str, recp_player: str):
        if not donor_player or not recp_player or donor_player == recp_player:
            return {'Error': 'Invalid From and To players'}
        if donor_player not in self.player_to_tixs or len(self.player_to_tixs[donor_player]) < num_of_tix:
            return {'Error': 'Donor player does not have enough tickets'}
        self.__transfer_lock.acquire()
        for _ in range(num_of_tix):
            curr_tix = next(iter(self.player_to_tixs[donor_player]))
            self.__add_ticket_to_player(recp_player, curr_tix)

        self.__check_n_remove_player(donor_player)

        self.__transfer_lock.release()
        return {'Success: Transferred {} tickets from {} to {}'.format(num_of_tix, donor_player, recp_player)}

    def draw_winner(self):
        if len(self.tix_to_player) == 0:
            return {'Error': 'No tickets in the game yet!!!'}

        self.__player_update_lock.acquire()
        self.__tix_update_lock.acquire()
        self.__transfer_lock.acquire()

        winner_tix = random.choice(list(self.tix_to_player.keys()))
        winner_player = self.tix_to_player[winner_tix]
        del self.tix_to_player[winner_tix]
        self.player_to_tixs[winner_player].remove(winner_tix)

        self.__transfer_lock.release()
        self.__tix_update_lock.release()
        self.__player_update_lock.release()
        return {'Winner': 'Hurreyy!!! Congratulations {}:{}'.format(winner_player, winner_tix)}
