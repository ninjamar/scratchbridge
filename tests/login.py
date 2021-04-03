import requests 
import json
def login(user,password):
  headers = {
    'Referer': 'https://scratch.mit.edu/',
    'Origin': 'https://scratch.mit.edu',
    'X-Requested-With': 'XMLHttpRequest',
  }
  s = requests.Session() 
  r = s.get('https://scratch.mit.edu/csrf_token/', headers=headers)
  CSRF = r.cookies.get_dict()['scratchcsrftoken']
  headers['X-CSRFToken'] = CSRF 
  s.headers.update(headers) 
  r = s.post('https://scratch.mit.edu/accounts/login/', data=json.dumps({'username':user, 'password':password}))
  return r,CSRF
