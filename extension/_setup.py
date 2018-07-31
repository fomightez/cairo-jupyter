# -*- coding: utf-8 -*-
from setuptools import setup

setup_kwargs=dict(
    name='cairo-jupyter',
    packages=['cairo_jupyter'],
    install_requires=["jupyter-pip"],
)

try:
    from jupyterpip import cmdclass
    setup_params['cmdclass'] = jupyterpip
except:
    cmdclass=setup

setup(**setup_kwargs)


