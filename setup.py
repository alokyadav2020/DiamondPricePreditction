from setuptools import find_packages,setup
from typing import List


HYPHEN_R_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('/n','') for req in requirements]

        if HYPHEN_R_DOT in requirements:
            requirements.remove(HYPHEN_R_DOT)

        return requirements




setup(
     name='DiamondPricePrediction',
     version='0.0.1',
     author='Alok Ranjan',
     author_email='10alokranjan@gmail.com',
     install_requires=get_requirements('requirements.txt'),
     packages=find_packages()


)