from setuptools import setup, find_packages
from typing import List

# Define a function to get the requirements from a file

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    Reads the requirements from a file and returns them as a list.
    """
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# This is the setup script for the ML project.
# It defines the package metadata and dependencies.

setup(
    name="mlproject",
    version="0.0.1",
    author="Joshua Pedro",
    author_email="joshfpedro@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)