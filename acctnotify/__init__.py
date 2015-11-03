import os
import yaml

version = '0.0.1'

templates_dir = os.getenv('NOTIFIER_TEMPLATES_DIR',
                          os.path.join(os.path.expanduser('~'),
                                       '.acctnotifier', 'templates'))

services_config_file = os.getenv('NOTIFIER_SERVICES_CONFIG',
                                 os.path.join(os.path.expanduser('~'),
                                              '.acctnotifier', 'config'))

users_config_dir = os.getenv('NOTIFIER_USERS_CONFIG',
                             os.path.join(os.path.expanduser('~'),
                                          '.acctnotifier', 'users'))

services_config = None

with open(services_config_file, 'r+') as fh:
    services_config = yaml.load(fh)
    for svc in services_config:
        if 'template' not in services_config[svc]:
            services_config[svc]['template'] = '{}.email'.format(svc)
    