# The New Account Notifier

We have a really fancy, nifty account provisioning and notification system.
Unfortunately, we also have a couple of external services that are stuck in
the stone age and do not provide any sort of provisioning or invitation API,
so I wind up having to go manually through each service for new employees.

I have tried to keep my emails consistent, but there's invariably drift over
time. Not anymore: create a template and a config, then define a user's new
accounts and let 'er rip!

# Usage

Installation:

    python setup.py install

Configuration:

`~/.acctnotify/config` contains a list of available services in YAML format.

```
---
  servicename:
    name: Some Service
    url: http://someurl
    administrator: Some Person <someone@somewhere.com>
    email_subject: This Appears in the Email Subject
    src_addr: some_email@domain.tld
    template: templatename.email
  ...
```

`template` is optional and defaults to `servicename.email`.

`~/.acctnotify/templates` contains jinja2 templates that will be used for the
email body. They should look something like this:

```
You've been granted access to {{ service.name }}.

URL: {{ service.url }}
Username: {{ account.username }}
Password: {{ account.password }}

Please take a moment to log in and set your own password. If you have
any questions about this service, please contact {{ service.administrator }}.

Any other information a user many need to know can be included as well.
```

And lastly, you'll make a yaml file for the user that includes his email and
login information for each site.

```
---
  name: Some User
  emails:
    primary: their_email@domain.tld
  accounts:
    servicename:
      username: someuser
      password: somepassword
```

The keys in `accounts` must match services in the config above.