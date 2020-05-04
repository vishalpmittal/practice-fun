"""
    tag: list

    Meetings Bonanza
    Description
    Google Calendar, Outlook, iCal has been banned from your company! 
    So an intrepid engineer has decided to roll their own implementation. 
    Unfortunately one major missing feature is the ability to find out what time slots 
    are free for a particular individual.

    Given a list of time blocks where a particular person is already booked/busy, a 
    start and end time to search between, a minimum duration to search for, find all 
    the blocks of time that a person is free for a potential meeting that will last 
    the aforementioned duration.

    Given: start_time, end_time, duration, meetings_list -> suggested_meeting_times

    Let's assume we abstract the representation of times as simple integers, so a 
    valid time is any valid integer supported by your environment. 
    Here is an example input:
    meetings_list: [3,20], [-2, 0], [0,2], [16,17], [19,23], [30,40], [27, 33]
    start_time: -5
    end_time: 27
    min_duration: 2
    
    expected answer: [-5, -2], [23,27]
    
    Feel free to represent the meetings however you would like, i.e. List of Lists, Lists of Objects etc.
"""


# MeetingList, StartTime, EndTime, MinDuration
def find_slots(ML, ST, ET, MD):
    ML = sorted(ML, key=lambda x: x[0])
    if not ML or MD < 1:
        return []

    RTSL = []  # Result Time Slot List
    CET = ST  # Current End Time
    for i, ts in enumerate(ML):
        # print(i, ts, RTSL, CET)
        if ts[0] > ET:
            return RTSL
        if CET + MD < ts[0]:
            RTSL.append([CET, ts[0]])
        CET = max(CET, ts[1])

    if CET + MD < ET:
        RTSL.append([CET, ET])

    return RTSL


meetings = [[3, 20], [-2, 0], [0, 2], [16, 17], [19, 23], [30, 40], [27, 33]]
assert find_slots(meetings, -5, 27, 2) == [[-5, -2], [23, 27]]
assert find_slots(meetings, 10, 27, 2) == [[23, 27]]
assert find_slots(meetings, 24, 27, 2) == [[24, 27]]
assert find_slots(meetings, -5, 50, 6) == [[40, 50]]
