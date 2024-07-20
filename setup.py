from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]  ## this line is used to replace the enocountered "\n" with a "" 
                                                                      ## while we go the next line of requirements.txt
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)              
    return requirements                                                
                                                        
setup(
name = 'mlproject',
version = '0.0.1',
author = 'Saad',
author_email = 'mdsaad7803@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt') 
    
    
)