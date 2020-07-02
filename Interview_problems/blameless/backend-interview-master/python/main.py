import sys
import time
import argparse
from internal.events import EventStream
from solution.monitor import get_service_monitor

class ProbabilityRange(object):
    def __eq__(self, other):
        return 0.0 <= other <= 1.0
    def __str__(self):
        return '0.0 <= val <= 1.0'

parser = argparse.ArgumentParser(description='Change and acceess event stream processor')
parser.add_argument('--seed', type=int, default=1337, help='Random number generator seed value')
parser.add_argument('--max-events', type=int, default=100000, help='Max number of events to generate')
parser.add_argument('--prob-bug', type=float, default=0.1, choices=[ProbabilityRange()], help='Probability change introduces bug')
parser.add_argument('--prob-error', type=float, default=0.05, choices=[ProbabilityRange()], help='Probability of a request error, given a bug has been introduced')
args = parser.parse_args()

if __name__ == '__main__':
    curr_time = time.time()
    # name, start_time, seed, change_rate, prob_of_bug, prob_of_error):
    # Fixing change rate to 1 every 10 seconds tro keep things simple
    event_stream = EventStream("foo", curr_time, args.max_events, args.seed, 0.1, args.prob_bug, args.prob_error)

    # It is assumed that you have implemented the functions below:
    #
    # event_stream is of type EventStream (see internal.events.EventStream)
    #
    # You create an object that is instantiated and assigned to service_monitor.  This
    # class must implement mttr(), api_histogram() and incident_details() as described
    # in README.md
    service_monitor = get_service_monitor(event_stream)
    print(service_monitor.mttr())
    print(service_monitor.api_histogram())
    print(service_monitor.incident_details())
