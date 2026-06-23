from setuptools import find_packages,setup
from Utils import Function
setup(
    name="mlproject",
    version="0.0.2",
    author="maheshwaranram",
    author_email="maheshwaran.er@gmail.com",
    packages=find_packages(),
    install_requires=Function.get_requirements("requirements.txt")
)