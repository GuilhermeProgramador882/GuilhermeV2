import os
import sys
import django


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_gastos.settings')
django.setup()

from django.test import Client
from django.conf import settings

c = Client()

print('LOGOUT_REDIRECT_URL =', getattr(settings, 'LOGOUT_REDIRECT_URL', None))

resp = c.get('/logout/')
print('GET /logout/ -> status:', resp.status_code)
print('GET redirect_chain:', resp.redirect_chain)

resp_post = c.post('/logout/')
print('POST /logout/ -> status:', resp_post.status_code)
print('POST redirect_chain:', resp_post.redirect_chain)


content = resp.content.decode('utf-8')
print('\nResponse content snippet:')
print(content[:500])
