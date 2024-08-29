from setuptools import find_packages, setup
from typing import List

hyphen_e_dot="-e ."

def get_requirements(filepath:str) -> List[str] :
    """
    This will return a list of requirements.
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements


setup(
    name="mlproj",
    version="0.0.1", 
    author="Gaurav",
    author_email="mailgaurav77@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)