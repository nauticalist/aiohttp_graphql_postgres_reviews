import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(os.path.dirname(__file__), 'info', '__init__.py')

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp==3.7.4',
    'aiohttp_cors==0.7.0',
    'alembic==1.1.0',
    'aiopg==0.16.0',
    'SQLAlchemy==1.3.8',
    'psycopg2-binary==2.8.3',
    'gunicorn==19.9.0',
    'graphql-core<3,>= 2.1',
    'graphene==2.1.8',
    'argparse==1.4.0',
    'aiohttp-graphql==1.0.0',
    'trafaret-config==2.0.2',
    'trafaret==1.2.0',
]


setup(
    name='info',
    version=read_version(),
    description='info about myself',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
