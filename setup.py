from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="rb-utils",  # what you pip install, name in PyPi
    version="0.0.1",
    description="Collection of utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["say_hello"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v3",
    ],
    install_requires=[],
    extras_require={"dev": ["pytest>=3.6",],},
    url="https://github.com/rbiswasfc/utils",
    author="Raja Biswas",
    author_email="rajabiswas92@outlook.com",
)
