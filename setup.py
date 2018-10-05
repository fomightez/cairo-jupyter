# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup_kwargs=dict(
    name='cairo-jupyter',
    packages=find_packages('extension'),
    package_dir={'': 'extension'},
    install_requires=["jupyter-pip"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "nbval"],
)

try:
    from jupyterpip import cmdclass
    setup_params['cmdclass'] = jupyterpip
except:
    cmdclass=setup

setup(**setup_kwargs)



