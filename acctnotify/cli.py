import os
import sys
import click

CONTEXT_SETTINGS = dict(auto_envvar_prefix='NOTIFIER')


class Context(click.Context):
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)

@click.command()
@click.argument('email')
def notify_user(email):
    import yaml
    from acctnotify import users_config_dir
    
    user = None
    
    user_config = os.path.join(users_config_dir, email)
    if not os.path.exists(user_config):
        print '[ERROR] User config not found at {}'.format(user_config)
        sys.exit(1)

    parsed_config = None
    with open(user_config) as fh:
        parsed_config = yaml.load(fh)
        
    if parsed_config:
        from acctnotify.user import User

        user = User(name=parsed_config['name'],
                    emails=parsed_config['emails'],
                    accounts=parsed_config['accounts'])
                    
        user.notify()
    else:
        print '[ERROR] Failed.'
        sys.exit(1)