
class VPException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'VPException, {0} '.format(self.message)
        else:
            return 'VPException has been raised'


# raise MyCustomError
raise VPException('We have a problem')
