import requests
import getpass
import pickle
from appdirs import AppDirs
from urllib.parse import urljoin

from .Settings import settings

def login():
    '''Log into a Plainview user account if not already logged in'''
    if logged_in():
        print('You are already logged in. Run \'plainview user logout\' to logout')
        return
    
    username = input('Plainview username:')
    password = getpass.getpass('Plainview password:')

    payload = {
        'username': username,
        'password': password
    }
    
    if not settings.PLAINVIEW_URL:
        print('Plainview URL not configured in settings. Run \'plainview settings edit\' to add')
        return
    
    r = requests.post(urljoin(settings.PLAINVIEW_URL, '/login'), data=payload)
    
    if r.status_code == 200:
        profile = r.cookies['profile']
        
        settings.PROFILE = profile
        
        print(f'You\'re now logged in as {profile.username}')
        return
    elif r.status_code == 400:
        print('Username or password incorrect. Please try again')
        return
    elif r.status_code == 429:
        print('Too many logins. Please try again later')
    
    
def logged_in():
   return False 
   
def logout():
    if not logged_in():
        print('You are not logged in. Run \'plainview user login\' to login')
        return
        
    r = requests.get(urljoin(settings.PLAINVIEW_URL, '/logout'))

    return False
    
def get_info():
    if not logged_in():
        print('You are not logged in. Run \'plainview user login\' to login')
        return
        
    r = requests.get(urljoin(settings.PLAINVIEW_URL, '/user'))

    return False

def signup():
    if logged_in():
        print('You are already logged in. Run \'plainview user logout\' to logout')
        return
    
    username = input('Plainview username: ')
    password = getpass.getpass('Plainview password:')

    payload = {
        'username': username,
        'password': password
    }
    
    if not settings.PLAINVIEW_URL:
        print('Plainview URL not configured in settings. Run \'plainview settings edit\' to add')
        return
    
    r = requests.post(urljoin(settings.PLAINVIEW_URL, '/signup'), data=payload)
    
    if r.status_code == 200:
        profile = r.cookies['profile']
        
        settings.PROFILE = profile
        
        print(f'Registration successful!\n You\'re now logged in as {profile.username}')
        return
    elif r.status_code == 409:
        print('Username already taken. Please try another one')
        return
    elif r.status_code == 429:
        print('Too many signups. Please try again later')

    return False