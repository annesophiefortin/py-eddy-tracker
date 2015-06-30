# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext as cython_build_ext

setup(
    name="pyeddytracker",
    version='2.0.3',
    description="Py-Eddy-Tracker libraries",
    classifiers=['Development Status :: Alpha',
                 'Topic :: Eddy',
                 'Programming Language :: Python'],
    keywords='eddy science',
    author='emason',
    author_email='emason@imedea.uib-csic.es',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=[
        'src/scripts/make_eddy_track_aviso.py',
        'src/scripts/make_eddy_track_CLS.py',
        'src/scripts/make_eddy_track_ROMS.py'],
    zip_safe=False,
    cmdclass={
        'build_ext': cython_build_ext,
    },
    ext_modules=[Extension("py_eddy_tracker.tools",
                           ["src/py_eddy_tracker/tools.pyx"])],
    setup_requires=[
        'numpy>=1.9'],
    install_requires=[
        'numpy>=1.9',
        'matplotlib>=1.2.1',
        'scipy>=0.15.1',
        'netCDF4>=1.1.0',
        'pyyaml',
        'pyproj',
        ],
)
