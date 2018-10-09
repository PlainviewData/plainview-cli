import os
import json
from appdirs import AppDirs
from urllib.parse import urljoin

from .utils import pretty_print_json

class Settings():

    def __init__(self, dirs=AppDirs("Plainview", "plainview-cli")):
        self.user_data_dir = dirs.user_data_dir
        self.user_cache_dir = dirs.user_cache_dir
        self.user_log_dir = dirs.user_log_dir
        
        self.plainview_config_file = os.path.join(self.user_data_dir, 'plainview-config.json')
        self.plainview_config = json.loads(open(self.plainview_config_file).read())

    def view(self):
        if os.path.isfile(self.plainview_config_file) == False:
            print('Settings have not been set! Run \'plainview settings edit\' to create')
        
        print(pretty_print_json(json.loads(open(self.plainview_config_file).read())))
        
    def edit(self):
        default_settings = {
            'plainview_url': 'localhost:8080'
        }
        if os.path.isfile(self.plainview_config_file) == False:
            os.makedirs(os.path.dirname(self.plainview_config_file))
            f = open(self.plainview_config_file, "w+")
            f.write(pretty_print_json(default_settings))
            f.close()
        os.system(self.plainview_config_file)

    @property
    def plainview_url(self):
        return self.plainview_config['plainview_url']
 