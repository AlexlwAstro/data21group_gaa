from configparser import ConfigParser
import json

available_info_categories = {
                            0: "postcode", 
                            1: "quality", 
                            2: "eastings", 
                            3: "northings", 
                            4: "country", 
                            5: "nhs_ha", 
                            6: "longitude",
                            7: "latitude", 
                            8: "european_electoral_region", 
                            9: "primary_care_trust", 
                            10: "region", 
                            11: "lsoa", 
                            12: "msoa",
                            13: "incode", 
                            14: "outcode", 
                            15: "parliamentary_constituency", 
                            16: "admin_district", 
                            17: "parish",
                            18: "admin_county", 
                            19: "admin_ward", 
                            20: "ced", 
                            21: "ccg",
                            22: "nuts", 
                            23: "codes"
                        }

config = ConfigParser()
config.read('postcode_config.ini')
postcodes = json.loads(config.get('POSTCODES', 'postcodes'))
inds_list = json.loads(config.get('CHOSENCATS', 'inds'))
print(type(postcodes), type(inds_list))
print(postcodes, inds_list)
