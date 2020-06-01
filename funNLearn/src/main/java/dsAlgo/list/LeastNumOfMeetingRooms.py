"""
    tag: meeting room, list

    m meetings
    meeting has id, starttime, endtime (both are in unix timestamp)
    Implement: List<Room> reserveRooms(List<Meeting>)
    should create least amount of Rooms, and that the meetings don't collide.
  
    Room is a object with id, List<Meeting> in that room
  
    for ex. 4 meetings. if they all overlap, you create 4 rooms
    for ex. 4 meetings, if they all dont overlap at all. you create 1 room

    Basically go through the list of meetings, use existing rooms if you can, 
    otherwise create a new virtual room on the fly. 
"""

from typing import List


class Meeting:
    __curr_meeting_id = 1

    def __init__(self, start_time, end_time):
        self.id = __curr_meeting_id
        __curr_meeting_id += 1
        self.start_time = start_time
        self.end_time = end_time


class Room:
    __curr_room_id = 1

    def __init__(self, id=None):
        self.id = id
        self.meetings = []
        self.last_meeting_end_time = None

    def add_meeting(self, mtng: Meeting):
        self.meetings.append(mtng)
        self.last_meeting_end_time = mtng.end_time

    @staticmethod
    def get_new_room():
        newroom = Room(Room.initial_id)
        __curr_room_id += 1
        return newroom


def reserveRooms(LOM: List[Meeting]) -> List[Room]:
    # initialize a queue of room with their current end times
    room_queue = []

    # sort meetings with their start time
    LOM = sorted(LOM, key=lambda x: x.start_time)

    for curr_meeting in LOM:
        cur_mtn_room = None
        i = 0
        while not cur_mtn_room and i < len(room_queue):
            if room_queue[i].last_meeting_end_time <= curr_meeting.start_time:
                cur_mtn_room = room_queue[i]
                room_queue.pop(i)
            else:
                i += 1

        if not cur_mtn_room:
            cur_mtn_room = Room.get_new_room()

        cur_mtn_room.add_meeting(curr_meeting)
        room_queue.append(cur_mtn_room)

    return room_queue
