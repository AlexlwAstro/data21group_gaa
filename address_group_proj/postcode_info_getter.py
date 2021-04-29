import requests
import json

from pprint import pprint
"""
post_code_req = requests.post('https://api.postcodes.io/postcodes/mk139hd')
print(type(post_code_req.headers))
print(type(post_code_req.content))  # class 'bytes'
print(post_code_req.json())
"""


class PostcodeInfo:
    def __init__(self, chosen_info_cat_ints):
        self.json_body, self.json_headers = self.add_list_of_postcodes()
        self.selected_keys = chosen_info_cat_ints


    def add_list_of_postcodes(self):
        add_postcode = True
        json_body_list = []
        while add_postcode:
            postcode_input_yn = input(
                'Would you like to retrieve info for a UK postcode (please enter \'y\' or \'n\')?\n')
            if postcode_input_yn == 'y':
                postcode_to_search = input('Which UK postcode do you need info for?')
                json_body_list.append(postcode_to_search)
            elif postcode_input_yn == 'n':
                print(f'List complete, length is {len(json_body_list)}')
                add_postcode = False
                break
            else:
                print(f"Sorry - You must type \'y\' or \'n\' - you have typed \'{postcode_input_yn}\'. Try again")

        json_body = json.dumps({"postcodes": json_body_list})
        headers = {'Content-Type': 'application/json'}
        return json_body, headers

    def select_info_to_show(self):
        post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=self.json_headers,
                                            data=self.json_body)
        selected_info_types = []
        for i in self.selected_keys:
            selected_info_types.append(available_info_categories[i])
        print(selected_info_types)
        print(post_multi_req)
        print(post_multi_req.json())
        json_results = post_multi_req.json()['result']  # json_results is a list object of the address
        print(json_results)
        for address_dict in json_results:
            for info_category in selected_info_types:
                print(info_category, address_dict['result'][info_category])

"""
    try:
        post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=self.json_headers,
                                       data=self.json_body)
        result_json = post_multi_req.json()
        results = result_json['result']
        print(len(results))
        for item in results:
            pprint(item)
    except ConnectionError:
        print('URL not recognised! Try again')
"""

available_info_categories = {
    0: "postcode", 1: "quality", 2: "eastings", 3: "northings", 4: "country", 5: "nhs_ha", 6: "longitude",
    7: "latitude", 8: "european_electoral_region", 9: "primary_care_trust", 10: "region", 11: "lsoa", 12: "msoa",
    13: "incode", 14: "outcode", 15: "parliamentary_constituency", 16: "admin_district", 17: "parish",
    18: "admin_county", 19: "admin_ward", 20: "ced", 21: "ccg", 22: "nuts", 23: "codes"
}

inds_list = [0, 4, 15]

postcode_print = PostcodeInfo(inds_list)
postcode_print.select_info_to_show()
