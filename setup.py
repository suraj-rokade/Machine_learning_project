from setuptools import setup
from typing import List



PROJECT_NAME = "husing_prediction"
VERSION = "0.0.3"
AUTHOR = "Suraj Rokade"
DESCRIPTION = "This is the first FSDS batch project"
PACKAGES=["housing"]
REQIOREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQIOREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup (
    name = PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages = PACKAGES,
    install_requirements=get_requirements_list()
)
