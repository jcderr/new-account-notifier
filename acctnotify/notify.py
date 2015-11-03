import boto.ses
from jinja2 import Environment, FileSystemLoader

from . import services_config, templates_dir


class Notifier(object):
    ses = None
    user = None
    templates = None

    def __init__(self, user=None):
        self.ses = boto.ses.connect_to_region('us-east-1')
        self.user = user
        self.templates = Environment(loader=FileSystemLoader(templates_dir))

    def notify(self):
        ''' triggers sending of emails representing new accounts '''
        for service in self.user.accounts:
            _svc = services_config[service]

            email_template = self.templates.get_template(_svc['template'])
            email_content = email_template.render(
                service=_svc,
                account=self.user.accounts[service]
            )

            self.ses.verify_email_address(_svc['src_addr'])
            self.ses.send_email(
                source=_svc['src_addr'],
                subject=_svc['email_subject'],
                to_addresses=self.user.emails['primary'],
                body=None,
                text_body=email_content,
            )
