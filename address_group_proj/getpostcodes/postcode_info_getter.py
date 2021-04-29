from postcode_variables import available_info_categories
import requests
import json
import sys


def get_postcodes() -> list:
    postcode_input = input('What postcode would you like info on? ')
    postcode_list = [postcode_input]

    while input('Would you like to look at another (Y/N)? ').lower() == 'y':
        postcode_input = input('What postcode would you like info on? ')
        postcode_list.append(postcode_input)

    return postcode_list


def post_postcodes(postcode_list: list) -> requests.Response:
    headers = {'Content-Type': 'application/json'}
    json_body = json.dumps({"postcodes": postcode_list})

    try:
        post_multi_req = requests.post("https://api.postcodes.io/postcodes", 
                                        headers=headers, 
                                        data=json_body)

    except ConnectionError:
        print('URL not recognised! Try again')
        
    if check_response(post_multi_req):
        if input('Would you like to try again (Y/N)? ').lower() == 'y':
            post_postcodes()
        
        else:
            print('Goodbye.')
            sys.exit(0)
    
    else:
        return post_multi_req


def check_response(response: requests.Response) -> bool:
    results = []
    for item in response.json()['result']:
        results.append(item['result'])
    
    if (None in results or response.status_code >= 400):
        print('Sorry one or more of your postcodes ' + 
                'were not found in the database.')

        return True

    else:
        return False


def select_info_to_show(post_response: requests.Response, 
                        selected_keys: list) -> None:

    selected_info_types = []
    for i in selected_keys:
        selected_info_types.append(available_info_categories[i])

    json_results = post_response.json()['result']

    for address_dict in json_results:
        for info_category in selected_info_types:
            print(info_category, address_dict['result'][info_category])
