from setuptools import setup, find_packages

setup(
    name='mypackage',
    version ='0.1',
    packages=find_packages(exclude=['test*']),
    license ='MIT',
    description = 'EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://gthub.com/<dineoxo>/<package_name>',
    author='<Dineo>',
    author_email='<dineoxmoela@gmail.com>'
)