import requests
import pickle
from urllib.parse import urljoin

from .Schema import is_valid
from .Schema import get_schema
from .Exceptions import NoPlainviewUrlError
from .utils import pretty_print_json
   
def login(username='', password='', plainview_url=''):
    '''Log into a Plainview user account if not already logged in'''
    if logged_in(plainview_url):
        print('You are already logged in. Run \'plainview user logout\' to logout')
        return
    
    payload = {
        'username': username,
        'password': password
    }
    
    if not plainview_url:
        raise NoPlainviewUrlError
    
    #if is_valid('user_login', payload) == False:
    #    raise Exception('Invalid login. ' + get_schema('user_login')['description'])
    
    r = requests.post(urljoin(plainview_url, '/login'), data=payload)
                
    if r.status_code != requests.codes.ok:
        print(f"Error: {r.json().get('message')}")
        return
    
    profile = r.cookies['profile']
    session.PROFILE = profile
    print(f"You're now logged in as {profile.username}")
    
    
def logged_in(plainview_url):
    '''Returns True or False whether a user is logged in'''
    return False
    #return (session.PROFILE is not None)
   
def logout(plainview_url):
    '''Log out of a Plainview account if logged in'''
    if not logged_in(plainview_url):
        print('You are not logged in. Run \'plainview user login\' to login')
        return
        
    r = requests.get(urljoin(plainview_url, '/logout'))

    return False
    
def get_info(plainview_url):
    '''Get user info if logged in'''
    
    if not logged_in(plainview_url):
        print('You are not logged in. Run \'plainview user login\' to login')
        return
        
    r = requests.get(urljoin(plainview_url, '/user'))
    
    if r.status_code != requests.codes.ok:
        print(f"Error: {r.json().get('message')}")
        return

    pretty_print_json(req.json())

    return False

def signup(username, password, plainview_url):
    '''Sign up for a Plainview account if not already logged in'''
    if logged_in(plainview_url):
        print('You are already logged in. Run \'plainview user logout\' to logout')
        return
    
    payload = {
        'username': username,
        'password': password
    }
    
    if not plainview_url:
        print('Plainview URL not configured in settings. Run \'plainview settings edit\' to add')
        return
    
    if is_valid('user_signin', payload, plainview_url) == False:
        raise Exception('Invalid signin. ' + get_schema(plainview_url)['description'])

    r = requests.post(urljoin(plainview_url, '/signup'), data=payload)
    
    if r.status_code != requests.codes.ok:
        print(f"Error: {r.json().get('message')}")
        return
    
    profile = r.cookies['profile']
    session.PROFILE = profile
    print(f'Registration successful!\nYou\'re now logged in as {profile.username}')
        