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

    try:
        # Open the requirements file
        with open(file_path) as f:

            # Read all lines from the file
            requirements = f.readlines()

            # Remove newline characters (\n)
            requirements = [req.replace("\n", "") for req in requirements]

            # Remove "-e ." because it should not be passed to install_requires
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

    except FileNotFoundError:
        # If requirements.txt is not found during build
        return []

    # Return the cleaned list of requirements
    return requirements


# setup() function defines package metadata and configuration
setup(

    # Name of the project package (this is the PyPI package name)
    name="afia-mongodbconnector",

    # Version of the package
    version="0.0.1",

    # Author information
    author="Afia Ishaq",
    author_email="afia.ishaq@riphah.edu.pk",

    # IMPORTANT for src layout
    # This tells Python that packages are inside the src folder
    packages=find_packages(where="src"),

    # Map root package directory to src
    package_dir={"": "src"},

    # Install dependencies listed in requirements.txt
    install_requires=get_requirements("requirements.txt"),
)