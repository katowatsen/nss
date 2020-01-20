from distutils.core import setup
from distutils.extension import Extension 
from Cython.Build import cythonize

extension = [Extension("core",
                      ["core.pyx"],) ]


setup(name="Natural Selection Simulator",
      ext_modules = cythonize(extension, language_level = "3"),)

from core import start
start()
