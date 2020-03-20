# -*- coding: utf-8 -*-
#
# For more info on Jupyter setup.py see:
# https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html
#
from setuptools import find_packages, setup

setup(
    name="cairo-jupyter",
    version="0.0.2",
    include_package_data=True,
    packages=find_packages("extension"),
    package_dir={"": "extension"},
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "nbval"],
    zip_safe=False,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        (
            "share/jupyter/nbextensions/cairo_jupyter",
            ["extension/cairo_jupyter/static/index.js"],
        ),
        # like `jupyter nbextension enable --sys-prefix`
        (
            "etc/jupyter/nbconfig/notebook.d",
            ["jupyter-config/nbconfig/notebook.d/cairo_jupyter.json"],
        ),
        # like `jupyter serverextension enable --sys-prefix`
        (
            "etc/jupyter/jupyter_notebook_config.d",
            ["jupyter-config/jupyter_notebook_config.d/cairo_jupyter.json"],
        ),
    ],
)

