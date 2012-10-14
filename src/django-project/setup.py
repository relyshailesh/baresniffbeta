from setuptools import setup, find_packages

setup(
    name='django-project',
    version='0.1',
    url='',
    packages=find_packages('.'),
    package_dir={'': '.'},
    install_requires=(
        'setuptools',
        'django-icetea',
    ),
)  


