import os

import yaml

from . import templates_dir, services_config


class TemplatesLoaderException(Exception):
    pass


class Templates(object):
    services = None

    def __init__(self):
        if not templates_dir:
            raise TemplatesLoaderException(
                'NOTIFIER_TEMPLATES_DIR must be configured')
        if not os.path.exists(templates_dir):
            raise TemplatesLoaderException(
                'Templates directory {} does not exist.'.format(templates_dir))

        if not services_config:
            raise TemplatesLoaderException(
                'NOTIFIER_SERVICES_CONFIG must be configured.')
        if not os.path.exists(services_config):
            raise TemplatesLoaderException(
                'Service config {} does not exist.'.format(services_config))

        with open(services_config) as fh:
            self.services = yaml.load(fh)

        for svc in self.services:
            if 'template' not in svc:
                self.services[svc]['template'] = '{}.email'.format(svc)

            _tmpl_path = os.path.join(templates_dir,
                                      self.services[svc]['template'])
            if not os.path.exists(_tmpl_path):
                raise TemplatesLoaderException(
                    '{} template file not found: {}'.format(
                        self.services[svc]['name'], _tmpl_path))
