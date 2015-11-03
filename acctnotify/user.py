from . import notify


class UserConfigurationException(Exception):
    pass


class User(object):
    accounts = {}
    name = None
    emails = {}

    def __init__(self, *args, **kwargs):
        if not all(k in kwargs for k in ('name', 'emails')):
            raise UserConfigurationException(
                'User object requires name and email')

        self.name = kwargs['name']

        if not type(kwargs['emails']) is dict:
            raise UserConfigurationException(
                'emails must be of type dict')

        if 'primary' not in kwargs['emails']:
            raise UserConfigurationException(
                'emails must contain a primary email')

        self.emails = kwargs['emails']

        if 'accounts' in kwargs:
            if type(kwargs['accounts']) is dict:
                self.accounts = kwargs['accounts']
            else:
                raise UserConfigurationException(
                    'accounts must be of type dict')

    def notify(self):
        _notifier = notify.Notifier(user=self)
        _notifier.notify()

    def __repr__(self):
        return '<User %s (%s)>' % (self.name, self.emails['primary'])
