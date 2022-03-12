from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-sourcetypes',
    version='0.0.1',
    author="Sam Willis",
    description="Python Source Code Types For Inline Syntax Highlighting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samwillis/python-inline-source/python-sourcetypes",
    py_modules=['sourcetypes'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[]
)
