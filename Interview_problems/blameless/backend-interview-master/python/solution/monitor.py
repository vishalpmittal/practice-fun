# Implement your solution here!
from internal.events import EventStream

EVENT_END_STR = 'end-of-stream'
EVENT_ACCESS_STR = 'access'
EVENT_CHANGE_STR = 'change'

INCIDENT = {'start': -1, 'end': -1, 'fix': '', 'break': ''}


class Access:
    DELIMITER = ' '
    RESP_SUCCESS = {'200'}
    RESP_FAILURE = {'500'}

    def __init__(self, access_str):
        access_attr = access_str.split(self.DELIMITER)
        self.ts = access_attr[0]
        self.verb = access_attr[1]
        self.resource = access_attr[2]
        self.response = access_attr[3]
        self.srvc_name = Service.get_srvc_name(self.resource)


class Change:
    DELIMITER = '\n'
    HASH_PREFIX = 'commit: '
    AUTHOR_PREFIX = 'Author: '
    DATE_PREFIX = 'Date: '
    SRVC_PREFIX = 'Service: '

    def __init__(self, commit_str):
        commit_attr = commit_str.split(Change.DELIMITER)
        self.commit = commit_attr[0].replace(self.HASH_PREFIX, '')
        self.author = commit_attr[1].replace(self.AUTHOR_PREFIX, '')
        self.date = commit_attr[2].replace(self.DATE_PREFIX, '')
        self.srvc_name = commit_attr[3].replace(self.SRVC_PREFIX, '')


class Service:
    resource_service_name_mapping = {}

    def __init__(self, s_name, email, verb, resource, slo, window):
        self.s_name = s_name
        self.email = email
        self.verb = verb
        self.resource = resource
        self.slo = slo
        self.window = window

        self.__last_access = None
        self.__last_change = None
        self.__accesses = [0 for _ in range(self.window)]
        self.__sli = self.slo
        self.__access_count = 0
        self.__curr_incident = None

        Service.resource_service_name_mapping[resource] = s_name

    @staticmethod
    def get_srvc_name(resource):
        return Service.resource_service_name_mapping[resource]

    def get_last_change(self):
        return self.__last_change

    def set_last_change(self, change: Change):
        self.__last_change = change

    def get_last_access(self):
        return self.__last_access

    def get_sli(self):
        return self.__sli

    def get_incident(self):
        return self.__curr_incident

    def set_incident(self, inc_json):
        self.__curr_incident = inc_json

    def get_accesses(self):
        return self.__accesses

    def update_last_access(self, access: Access):
        self.__accesses.pop(0)
        if access.response in Access.RESP_SUCCESS:
            self.__accesses.append(1)
        elif access.response in Access.RESP_FAILURE:
            self.__accesses.append(-1)
        else:
            self.__accesses.append(0)

        self.__access_count = min(self.window, self.__access_count + 1)
        self.__sli = sum(self.__accesses) / self.__access_count
        self.__last_access = access


class ServiceMonitor:
    def __init__(self, srvc_info_list):
        self.srvc_name_to_obj_dict = {}
        for srvc in srvc_info_list:
            self.srvc_name_to_obj_dict[srvc['name']] = Service(
                s_name=srvc['name'],
                email=srvc['email'],
                verb=srvc['verb'],
                resource=srvc['resource'],
                slo=srvc['slo'],
                window=srvc['window']
            )

        self.incidents = {}

    def __analyze_service_access(self, access_str):
        access = Access(access_str)
        srvc_obj = self.srvc_name_to_obj_dict[access.srvc_name]
        old_sli = srvc_obj.get_sli()
        srvc_obj.update_last_access(access)

        # if current sli is lower than the targeted slo
        if srvc_obj.get_sli() < srvc_obj.slo:
            # Incident already present for current situation
            if srvc_obj.get_incident() is not None:
                return

            # Create a new incident
            incident_obj = INCIDENT.copy()
            incident_obj['start'] = float(access.ts)
            if srvc_obj.get_last_change():
                incident_obj['break'] = srvc_obj.get_last_change().commit
            srvc_obj.set_incident(incident_obj)

            # add the incident to incidents dictionary
            s_incidents_list = self.incidents.get(srvc_obj.s_name, [])
            s_incidents_list.append(incident_obj)
            self.incidents[srvc_obj.s_name] = s_incidents_list

        # if current sli is greater than slo and past sli was less than slo
        # meaning incident has been recovered
        elif srvc_obj.get_sli() >= srvc_obj.slo > old_sli:
            # service fixed, update incident
            if not srvc_obj.get_incident():
                srvc_obj.set_incident(INCIDENT.copy())

            # Get the hash that broke it, and see if there is a newer hash
            break_hash = srvc_obj.get_incident()['break']
            last_srvc_hash = ''
            if srvc_obj.get_last_change():
                last_srvc_hash = srvc_obj.get_last_change().commit

            srvc_obj.get_incident()['end'] = float(access.ts)
            # if there was a newer change after breaking, then only update the fix hash
            if break_hash != last_srvc_hash:
                srvc_obj.get_incident()['fix'] = last_srvc_hash
            srvc_obj.set_incident(None)

    def __analyze_change(self, change_value):
        change = Change(change_value)
        self.srvc_name_to_obj_dict[change.srvc_name].set_last_change(change)

    def monitor_event_stream(self, eso: EventStream):
        print('Monitoring event Stream')
        event_obj_dict = eso.generate_event()
        while event_obj_dict['type'] != EVENT_END_STR:
            if event_obj_dict['type'] == EVENT_ACCESS_STR:
                self.__analyze_service_access(event_obj_dict['value'])
            elif event_obj_dict['type'] == EVENT_CHANGE_STR:
                self.__analyze_change(event_obj_dict['value'])
            event_obj_dict = eso.generate_event()

    def mttr(self):
        """
        :return: single value mean time to repair
        eg: 2.02
        """
        if not self.incidents:
            return 0

        rt = [inc['end'] - inc['start']
              for inc_list in self.incidents.values()
              for inc in inc_list
              if inc['end'] != -1
              ]
        return sum(rt) / len(rt)

    def api_histogram(self):
        """
        :return: dictionary
        { api-name : number of issues introduced by that api }
        {'nonexpulsion': 1, 'kioea': 1}
        """
        if not self.incidents:
            return {}
        return {evnt_name: len(evnt_list) for evnt_name, evnt_list in self.incidents.items()}

    def incident_details(self):
        """
        :return: dictionary
        {'nonexpulsion': [{
            'start': 1543443091.2745,
            'end': 1543443093.2896,
            'fix': '6d0080aaecbf4bd69f9b8962cb007e53',
            'break': '191b6ce2fc724b37a063e8b07065f80b'
        }], 'kioea': [{
            'start': 1543443093.3109,
            'end': -1,
            'fix': '',
            'break': 'b9936e80e621448fbef0802be647bd67'
        }]
        }
        """
        return self.incidents


def get_service_monitor(eso: EventStream):
    """
    :param eso: #EventStream Object
    :return: ServiceMonitor Object
    """
    sm = ServiceMonitor(eso.get_info())
    print('Read all service info objects')
    sm.monitor_event_stream(eso)
    return sm
