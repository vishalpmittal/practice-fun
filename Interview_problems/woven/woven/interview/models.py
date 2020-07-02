from django.db import models
import json, re


class EMail:
    def __init__(self, e_id, e_subject, e_from, e_to, e_date, e_body=None, e_parent_id=None, e_cc=None):
        self.id = re.sub('[<>]', '', e_id)
        self.subject = e_subject
        self.body = e_body
        self.from_ = re.sub('[<>]', '', e_from)
        self.to = e_to
        self.cc = e_cc
        self.date = e_date
        if e_parent_id:
            self.parent_id = re.sub('[<>]', '', e_parent_id)
        else:
            self.parent_id = None
        self.replies = None

    def __str__(self):
        return "---------------------------\n" \
               "id: {},\ndate: {},\nsubject: {},\nfrom: {},\nto: {},\ncc: {},\nbody: {},\nparent: {}\n".format(
            self.id, self.date, self.subject, self.from_, self.to, self.cc, self.body, self.parent_id
        )

    def add_reply(self, reply_email):
        if not isinstance(reply_email, EMail):
            return
        if not self.replies:
            self.replies = []
        self.replies.append(reply_email)

    def to_str_with_children(self, level=1):
        self_str = "\n{}{}{}".format('    ' * (level - 1), '>' * level, str(self))
        if not self.replies:
            return self_str

        for email in self.replies:
            self_str += email.to_str_with_children(level + 1)
        return self_str


class Inbox:
    def __init__(self):
        self.eid_2_obj_dict = {}
        self.top_level_email_ids = set()

    def load_emails_from_file(self, email_file='emails.json'):
        # Load all emails
        temp_dict = json.load(open(email_file))
        for e_id, e_body in temp_dict.items():
            self.eid_2_obj_dict[e_id] = EMail(
                e_id=e_id,
                e_subject=e_body['subject'],
                e_from=e_body['from'],
                e_to=e_body['to'],
                e_date=e_body['date'],
                e_body=e_body.get('body', None),
                e_parent_id=e_body.get('in-reply-to', None),
                e_cc=e_body.get('cc', None)
            )

        # set to store all reply ids
        children_id_set = set()

        # add all replies to parent emails, and create set of children email ids
        for e_id, e_obj in self.eid_2_obj_dict.items():
            p_id = e_obj.parent_id
            if p_id in self.eid_2_obj_dict:
                self.eid_2_obj_dict[p_id].add_reply(self.eid_2_obj_dict[e_id])
                children_id_set.add(e_id)
            else:
                e_obj.parent_id = None

        # get a set of top level email ids, with no parents
        for email_id in self.eid_2_obj_dict:
            if email_id not in children_id_set:
                self.top_level_email_ids.add(email_id)

    def get_all_emails(self):
        flt_inbox = ''
        for e_id, e_obj in self.eid_2_obj_dict.items():
            flt_inbox += str(e_obj)
        return flt_inbox

    def get_all_emails_threaded(self):
        threaded_inbox = ''
        for tl_e_id in self.top_level_email_ids:
            threaded_inbox += self.eid_2_obj_dict[tl_e_id].to_str_with_children()
        return threaded_inbox
