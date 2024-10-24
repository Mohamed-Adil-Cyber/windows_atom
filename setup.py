from setuptools import setup, find_packages

setup(
    name="windows_atom",
    version="1.0", 
    author="Mohamed Adil",
    author_email="MohamedAdilOfficial@gmail.com",
    description="A Python library to interact with the Windows atom table via ctypes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mohamed-Adil-Cyber/windows_atom",
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
