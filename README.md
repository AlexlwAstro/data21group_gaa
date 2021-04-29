# data21group_gaa

## **Contents of address_group_proj Package**

---------------------------------------

- Introduction 
- Requirements 
- Installation 
- Running the Package
- Supported Versions
- Error Handling
- Configuration 
- Troubleshooting 
- FAQ 
- Maintainers 

# **Introduction**

Welcome to our project! We have created a package that will return resulting details of a postcode or a multitude of postcodes. The user has an ability to input the given postcode and will be met with an opportunity to add another postcode with a Y/N answer that will be accepted. The user will have the capability to enter the postcode in lower or uppercase without an error message. 

We have created functions for the users to be able to view the outputted details in a human readable form with headings as keys.  



# **Requirements**

To run this package, firstly you will need to check which version of Python you have. If you are using a version of Python below Python 3, you will need to install: 

- **json** 



# **Installation**

For the installation of JSON, run the following code in the terminal: 

`$ python -m pip install json`


With the installation of address_group_proj package, it includes the installation of the requests package and therefore will not need to install requests manually. 

For the installation of address_group_proj package, run the following in the terminal: 

`$ python -m pip install address_group_proj` 


# **Running the Package**

The user can run the package to retrieve the intended postcodes via the following code: 

`$ python -m getpostcodes`


# **Supported Versions**

`address_group_proj` package is supported by versions of Python 3.7+. Prior to Python 3.7, the dictionary may not have been ordered. Therefore, the Python version 3.7 is recommended for optimum performance and up to date libraries. If the user is using Python 2, there may be manual installation of the `json` package. 


# **Error Handling**

Within this package, the authors have diligently handled the errors for you. If there is an error for the desired postcode, it will be met with an error message and give you the opportunity to reinsert the postcode. 


# **Configuration**

The authors of `address_group_proj` package have created a config file. This config file can be accessed through the package and the file is called config.ini



# **Troubleshooting**

The user cannot run the code unless it is installed as a module. 

Known Errors: 
- `TypeError` - Raised when a function or operation is applied to an object of incorrect type
- `AttributeError` - Raised when attribute assignment or reference fails
- `KeyError` - Raised when a key is not found in a dictionary



# **FAQ**

**Q. Can I run this package in Python 2?**

**A.** *Yes. You can run this package in Python 2 although it is not recommended. The user will lose out on capabilities such as the preinstalled json package as well as losing the functionality of ordered dictionary keys.*


**Q. Do I need to put spaces between the values in a postcode i.e. MC13 7GQ**

**A.** *No. The user does not necessarily need to put a space between values as the package accounts for this issue* 


**Q. Do I need to put the postcode in uppercase?**

**A.** *No. The package has accounted for users inputting upper and lowercase values in the postcode and will retrieve the correct response* 


**Q. I want to be able to search multiple postcodes. Is this possible?** 

**A.** *Yes. The user will input the first desired postcode, then will be met with a question stating if they would like to input another postcode in which the user can state `y/n`. This process will carry on repeating until the user states `n`. This will therefore indicte that the user is satisfied with inputted postcodes* 



# **Maintainers**
- __Giacomo Allen__ 
- __Alexander Lisboa-Wright__
- __Abanoub Hakeem__



# **Contributers**

- __Giacomo Allen__ 
- __Alexander Lisboa-Wright__
- __Abanoub Hakeem__


