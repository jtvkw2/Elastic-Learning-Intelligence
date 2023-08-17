from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'ELLIE Agent'
LONG_DESCRIPTION = 'This is a search agent based on elasticsearch'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="ellie",
    version=VERSION,
    author="Jacob Voyles",
    author_email="<jtvkw2@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'ellie'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
