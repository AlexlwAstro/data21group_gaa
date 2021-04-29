from getpostcodes.postcode_info_getter import get_postcodes, post_postcodes
import sys
from pprint import pprint

postcodes_list = get_postcodes()
post_multi_req = post_postcodes(postcodes_list)

result_json = post_multi_req.json()
results = result_json['result']

for item in results:
    pprint(item)

sys.exit(0)
