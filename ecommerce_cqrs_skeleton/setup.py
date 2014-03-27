from setuptools import setup, find_packages

setup( name='cqrs',
    version = '0.0.1',
    description = 'CQRS Ecommerce skeleton application',
    author = 'Dipak Yadav',
    author_email = 'dipak.kumar@clavax.com',
    url = 'https://github.com/commoncode/cqrs.io',
    keywords = ['tornado',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Tornado',
        'Operating System :: Ubuntu',
        'Programming Language :: Python',
    ],
    install_requires = [
        'tornado'
    ],
)
