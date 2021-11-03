from setuptools import setup

setup(
    name='Bromo',
    version='0.1',
    url='https://github.com/CoelhoBranco/bromo-lib',
    license='MIT',
    author='Leonardo Coelho',
    author_email='leonardo_leal15@outlook.com',
    description='lib to help with page loading strategy', 
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['selenium>=4.0.0']
   

)