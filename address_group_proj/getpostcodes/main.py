from getpostcodes.postcode_info_getter import get_postcodes, post_postcodes, select_info_to_show
from getpostcodes.postcode_variables import inds_list
import sys

postcodes_list = get_postcodes()
post_multi_req = post_postcodes(postcodes_list) 

select_info_to_show(post_multi_req, inds_list)

sys.exit(0)
