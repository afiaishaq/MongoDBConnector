# Import required functions from setuptools
# setup -> used to create the package
# find_packages -> automatically detects all packages in the project
from setuptools import setup, find_packages

# Used for type hinting (good practice in professional Python projects)
from typing import List


# Constant used to remove '-e .' from requirements
# '-e .' means install the project in editable mode
HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements.txt file
    and returns a list of dependencies needed
    to run the project.
    """

    requirements = []

    # Open the requirements file
    with open(file_path) as f:

        # Read all lines from the file
        requirements = f.readlines()

        # Remove newline characters (\n)
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove "-e ." because it should not be passed to install_requires
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    # Return the cleaned list of requirements
    return requirements


# setup() function defines package metadata and configuration
setup(

    # Name of the project package
    name="mlops_project",

    # Version of the package
    version="0.0.1",

    # Author name
    author="Afia Ishaq",

    # Author email
    author_email="your_email@gmail.com",

    # Automatically find all packages inside the project
    # Example: src/components, src/database, src/utils
    packages=find_packages(),

    # Install dependencies listed in requirements.txt
    install_requires=get_requirements("requirements.txt")
)