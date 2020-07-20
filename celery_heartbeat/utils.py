from django.conf import settings

UNSET = type('UNSET', (object,), {})  # used as non-None default value


def get_setting(name, default=UNSET):

    try:
        return getattr(settings, name)
    except AttributeError:
        pass

    if default is not UNSET:
        return default

    raise ValueError('You must set %s.' % name)
