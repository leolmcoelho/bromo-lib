from setuptools import setup
import setuptools

setup(
    name='bromo',
    version='0.2.1',
    url='https://github.com/CoelhoBranco/bromo-lib',
    license='GNU GPLv3',
    author='Leonardo Coelho',
    author_email='leonardo_leal15@outlook.com',
    description='lib to help with page loading strategy', 
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
        ],
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'), 
    python_requires='>=3.7',
    include_package_data=True
    #install_requires=['selenium>=4.0.0']

)