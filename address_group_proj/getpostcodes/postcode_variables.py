from configparser import ConfigParser

config = ConfigParser()
config.read('getpostcodes/config.ini')

inds_list = config['CHOSEN CATEGORIES']['INDEX'].split(',')

info_categories = [config['CATEGORIES'][index.strip()] for index in inds_list]

postcodes = [config['POSTCODES'][value.upper()] 
            for value in list(config['POSTCODES'])]
