"""
Author: Jose Stovall | oitsjustjose
"""

from setuptools import setup
from Cython.Build import cythonize

import os

setup(
    ext_modules = cythonize("logger.pyx"),
    compiler_directives={'language_level' : "3"}
)

setup(
    ext_modules = cythonize("docker_mgr.pyx"),
    compiler_directives={'language_level' : "3"}
)

print("Moving files to outdir")

for file in os.listdir("."):
    if not os.path.isdir(file):
        if not (file.endswith(".py") or file.endswith(".pyx")):
            os.rename(file, f"./out/{file}")
