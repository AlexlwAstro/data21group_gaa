from getpostcodes.postcode_info_getter import post_postcodes, select_info_to_show
from getpostcodes.postcode_variables import postcodes 
import sys

post_multi_req = post_postcodes(postcodes) 

select_info_to_show(post_multi_req)

sys.exit(0)
