# Copyright (C) 2018 O.S. Systems Software LTDA.

from setuptools import find_packages, setup

from updatehub import get_version


setup(
    name='updatehubagentsdk',
    description="UpdateHub's agent SDK for Python",
    keywords='industrial-linux embedded-linux embedded firmware-updates linux update-service',  # nopep8
    version=get_version(),
    packages=find_packages(),
    install_requires=[],
    author='O.S. Systems Software LTDA',
    author_email='contato@ossystems.com.br',
    url='http://www.ossystems.com.br',
    license='MIT',
    zip_safe=False,
)
