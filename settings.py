PLATFORM = 'linux'
DRIVER = 'phantomjs'
WEB_DRIVER_WAIT_TIMEOUT = 120  # 2 minutes
RUT = ''
CLAVE = ''

try:
    from local_settings import *
except:
    pass
