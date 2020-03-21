"""
    Tag: algo
    Finite state machine, FSM, Finite Automata
"""

# Generic State class
class State(object):
    def __init__(self):
        print("Processing current state:", str(self))

    def on_event(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__


# Two states of the mobile device: LockedState
class LockedState(State):
    def on_event(self, event):
        if event == "pin_entered":
            return UnlockedState()
        return self


# Two states of the mobile device: UnlockedState
class UnlockedState(State):
    def on_event(self, event):
        if event == "device_locked":
            return LockedState()
        return self


class SimpleDevice(object):
    def __init__(self):
        self.state = LockedState()

    def on_event(self, event):
        self.state = self.state.on_event(event)


device = SimpleDevice()
device.on_event("device_locked")
print(device.state)
device.on_event("pin_entered")
print(device.state)
device.on_event("device_locked")
print(device.state)
device.on_event("pin_entered")
print(device.state)
device.on_event("pin_entered")
print(device.state)
