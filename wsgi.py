import os



workers = int('2')

threads = int('4')

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = '0.0.0.0:8080'



forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }