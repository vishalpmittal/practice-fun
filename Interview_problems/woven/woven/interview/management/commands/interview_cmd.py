# -*- encoding: utf-8 -*-
# Copyright © 2019 VMware, Inc.  All rights reserved.
# VMware Confidential

import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from interview.rest_worker import RESTWorker
from interview.models import Inbox

logger = logging.getLogger("stats")


class Command(BaseCommand):
    """
    Usage: manage.py interview_cmd [options]
    """
    option_list = BaseCommand.option_list + (
        make_option(
            '--inbox-type',
            dest='inbox_type',
            action='store',
            type='string',
            help='--inbox-type=flat/threaded'
        ),
    )

    def handle(self, *args, **options):
        inbox = Inbox()
        inbox.load_emails_from_file()

        if options['inbox_type'] == 'flat':
            print inbox.get_all_emails()
        elif options['inbox_type'] == 'threaded':
            print inbox.get_all_emails_threaded()
        else:
            print 'No parameter, for help: python manage.py interview_cmd --help'
