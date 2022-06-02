from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    img_url = "https://raw.githubusercontent.com/samwillis/python-inline-source/main/sourcetypes/docs/examples.png"
    long_description = long_description.replace("(sourcetypes/docs/examples.png)", f"({img_url})")

setup(
    name='sourcetypes',
    version='0.0.3',
    author="Sam Willis",
    description="Python Source Code Types For Inline Syntax Highlighting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samwillis/python-inline-source/sourcetypes",
    py_modules=['sourcetypes'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'typing-extensions>=4.2.0',
    ]
)
