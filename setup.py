from setuptools import setup

setup(
    name = 'labgeeks-sybil',
    version = '1.0',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks_sybil',
    description = 'The search app for the labgeeks suite of student staff management tools.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_sybil',],
    install_requires = [
        'setuptools',
        'pillow',
        'South==0.7.3',
        'Whoosh==2.4.1',
        'django-haystack==1.2.7',

    ],
)
