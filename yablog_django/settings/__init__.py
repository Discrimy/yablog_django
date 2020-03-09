import os


if os.environ.get('DJANGO_DEV') is not None:
    from .dev import *
else:
    from .prod import *
