import sys
import argparse
import getpass

from .User import login as user_login
from .User import logout as user_logout
from .User import get_info as user_get_info
from .User import signup as user_signup

from .Exceptions import NoPlainviewUrlError

from .Settings import Settings

def ExecuteCommand():
    '''Accepts command line arguments and executes them'''
    parser = argparse.ArgumentParser(description='Command Line Interface for Plainview')
    subparsers = parser.add_subparsers()
    
    parser_user = subparsers.add_parser('user', help='Login/logout and general user functions')
    parser_user.add_argument('user_command', type=str, help='The user command', choices=['login', 'logout', 'info', 'signup'])

    parser_archive = subparsers.add_parser('archive', help='Interact with Plainview archives')
    parser_archive.add_argument('archive_command', type=str, help='The user command', choices=['new', 'view', 'list'])

    parser_archive = subparsers.add_parser('settings', help='Interact with Plainview archives')
    parser_archive.add_argument('settings_command', type=str, help='The user command', choices=['view', 'edit'])
    
    commands = parser.parse_args()
    
    settings = Settings()
    try:
        if 'user_command' in commands:
            user_command = commands.user_command
            if user_command == 'login':
                username = input('Plainview username:')
                password = getpass.getpass('Plainview password:')
                user_login(username=username, password=password, plainview_url=settings.plainview_url)
            elif user_command == 'logout':
                user_logout(plainview_url=settings.plainview_url)
            elif user_command == 'info':
                user_get_info(plainview_url=settings.plainview_url)
            elif user_command == 'signup':
                username = input('Plainview username:')
                password = getpass.getpass('Plainview password:')
                user_signup(username=username, password=password, plainview_url=settings.plainview_url)
                
        if 'archive' in commands:
            archive_command = commands.archive_command
            
        if 'settings_command' in commands:
            settings_command = commands.settings_command
            
            if settings_command == 'view':
                settings.view()
            elif settings_command == 'edit':
                settings.edit()
    except NoPlainviewUrlError:
        print('Plainview URL not set in settings. Run \'plainview settings edit\' to set')
