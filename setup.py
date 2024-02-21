from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['testa*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Afezhus/mypackage',
    author='Abdulafeez Hussain',
    author_email='abdulafeezhussain@gmail.com'
)