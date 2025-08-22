# Will be responsible to create the whole machine learning project as a package
from setuptools import find_packages,setup
from typing import List


Hyp = '-e .'
def get_reqirements(file_path:str)->List[str]:
    '''
    Returning the requirements.txt as a list
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if Hyp in requirements:
            requirements.remove(Hyp)

setup(
name='E_to_E',
version='0.1',
author='Dhanesh',
author_email='panchariyadhanesh@gmail.com',
packages=find_packages(),
install_requires=get_reqirements('requirements.txt')
)